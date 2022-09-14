



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

@app.route('/producto_detalle/<int:id_product>')
def producto_detalle(id_product):
    formulario = {
        "id":id_product
    }

    producto = Products.get_by_id(formulario)

    return render_template('detalle_producto.html', producto = producto)

@app.route('/eliminar/<int:id_producto>')
def eliminar(id_producto):
    formulario = {
        "id":id_producto
    }

    Products.delete(formulario)

    return redirect('/mostrar_productos')

@app.route('/actualizar/producto/<int:id_producto>')
def actualizar_poema(id_producto):
    if not session:
        return redirect('/')

    formulario = {
        "id":id_producto
    }

    producto = Products.get_by_id(formulario)
    return render_template('actualizar_producto.html', producto = producto)

    
@app.route('/modificar_producto', methods=['POST'])
def modificar_producto():
    if not session:
        return redirect('/')

    formulario = {
        "name": request.form['name'],
        "price": request.form['price'],
        "description": request.form['description'],
        "presentation":request.form['presentation'],
        "user_id":session['users_id'],
        "id":request.form['producto_id']
    }

    Products.updated(formulario)
    return redirect('/mostrar_productos')