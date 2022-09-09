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