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