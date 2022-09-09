from Flask_app.config.mysqlconnection import connectToMySQL

class Review:

    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.likes = data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.product_id = data['product_id']
        self.user_id = data['user_id']
        