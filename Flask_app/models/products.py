from Flask_app.config.mysqlconnection import connectToMySQL

class Products:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description = data['description']
        self.presentacion = data['presentacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

@classmethod
def save(cls,formulario):
    query = "INSERT INTO products(name, price, description, presentacion, user_id) VALUES (%(name)s, %(price)s, %(description)s, %(presentacion)s, %(users_id)s)"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result

@classmethod
def delete(cls,formulario):
    query = "DELETE * FROM products WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result

@classmethod
def updated(cls, formulario):
    query = "UPDATE products SET name = %(name)s, price = %(price)s, description = %(description)s, presentacion = %(presentacion)s, users_id = %(user_id)s WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query, formulario)
    return result