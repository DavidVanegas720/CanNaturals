from Flask_app.config.mysqlconnection import connectToMySQL

class Products:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description = data['description']
        self.presentation = data['presentation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO products(name, price, description, presentation, user_id) VALUES (%(name)s, %(price)s, %(description)s, %(presentation)s, %(user_id)s)"
        result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
        print("----------------")
        return result

    @classmethod
    def delete(cls,formulario):
        query = "DELETE * FROM products WHERE id = %(id)s"
        result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
        return result

    @classmethod
    def updated(cls, formulario):
        query = "UPDATE products SET name = %(name)s, price = %(price)s, description = %(description)s, presentation = %(presentation)s, users_id = %(user_id)s WHERE id = %(id)s"
        result = connectToMySQL('proyecto_grupal').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products"
        result = connectToMySQL('proyecto_grupal').query_db(query)
        print(result)
        return result