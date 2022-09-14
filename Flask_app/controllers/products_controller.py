

from Flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from Flask_app import app

from Flask_app.models.products import Products
from Flask_app.models.users import Users

@app.route('/registrar_producto')
def registrar_producto():
    return render_template('registrar_producto.html')

@app.route('/guardar_producto', methods=['POST'] )
def guardar_producto():
    
    if not session:
        return redirect('/')

    formulario = {
        "name": request.form['name'],
        "price": request.form['price'],
        "description": request.form['description'],
        "presentation":request.form['presentation'],
        "user_id":session['users_id']
    }

    Products.save(formulario)

    return redirect('/principal')


@app.route('/mostrar_productos')
def mostrar_producto():
    print("-----------")
    data = Products.get_all()
    return render_template('mostrar_producto.html', data = data)