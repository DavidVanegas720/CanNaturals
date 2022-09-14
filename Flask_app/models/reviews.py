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
        

@classmethod
def save(cls,formulario):
    query = "INSERT INTO reviews(comment, likes, product_id, user_id ) VALUES (%(comment)s, %(likes)s, %(product_id)s, %(user_id)s)"
    result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
    return result

@classmethod
def delete(cls,formulario):
    query = "DELETE * FROM reviews WHERE id = %(id)s"
    result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
    return result

@classmethod
def updated(cls, formulario):
    query = "UPDATE reviews SET comment = %(comment)s, likes = %(likes)s, product = %(product)s, user_id = %(user_id)s WHERE id = %(id)s"
    result = connectToMySQL('proyecto_grupal').query_db(query, formulario)
    return result

