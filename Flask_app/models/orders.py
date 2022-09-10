from Flask_app.config.mysqlconnection import connectToMySQL

class Orders:

    def __init__(self,data):
        self.id = data['id']
        self.productos = data['productos']
        self.total = data['total']
        self.direccion = data['direccion']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def save(cls,formulario):
    query = "INSERT INTO orders(productos, total, direccion, user_id,) VALUES (%(productos)s, %(total)s, %(direccion)s, %(user_id)s)"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result

@classmethod
def delete(cls,formulario):
    query = "DELETE * FROM orders WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result

@classmethod
def updated(cls, formulario):
    query = "UPDATE orders SET productos = %(productos)s, total = %(total)s, direccion = %(direccion)s, user_id = %(user_id)s WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query, formulario)
    return result