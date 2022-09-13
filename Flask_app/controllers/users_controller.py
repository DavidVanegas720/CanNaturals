
from Flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
from Flask_app.models.users import Users

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def registro():
    return render_template('registro.html')


@app.route('/registro', methods=['POST'])
def registros():

    if len(request.form['nombre']) < 5:
        return  jsonify(message='Escribe tu nombre ')
            
    if len(request.form['apellido']) <1:
        return jsonify(message='Escribe tu apellido')

    if not EMAIL_REGEX.match(request.form['email']):
        return jsonify(message='Email invalido')

    if Users.get_by_email(request.form):
        return jsonify(message='El email ya existe')

    if len(request.form['contraseña']) < 6:
        return jsonify(message='La contraseña debe contener al menos 6 caracteres')

    if request.form['contraseña'] != request.form['confirma_contraseña']:
        return jsonify(message='Las contraseñas no coinciden')


    secret = bcrypt.generate_password_hash(request.form['contraseña'])

    formulario = {
        "first_name": request.form['nombre'],
        "last_name": request.form['apellido'],
        "email": request.form['email'],
        "password":secret
    }

    Users.save(formulario)

    return jsonify(message='validado')


# @app.route('/inicio')
# def inicio():
#     return redirect('/')



@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/inicio', methods=['POST'])
def inicio():

    if len(request.form["email"]) < 1:
        return jsonify(message="Email requerido")


    user = Users.get_by_email(request.form)
    if not user:
        return jsonify(message='Email no registrado')

    if len(request.form['password']) < 1:
        return jsonify(message="Escribe tu contraseña")

    if not bcrypt.check_password_hash(user[0]["password"],request.form["password"]):
        return jsonify(message="Contraseña incorrecta")

    session['usuario_id'] = user[0]['id']
            
    return jsonify(message='validado')