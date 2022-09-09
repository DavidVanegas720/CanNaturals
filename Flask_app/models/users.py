
from Flask_app.config.mysqlconnection import connectToMySQL


class Users:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.user_type = data['user_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def save(cls,formulario):
    query = "INSERT INTO users(first_name, last_name, email, password, user_type) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(user_type)s"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result

@classmethod
def get_user_by_id(cls,formulario):
    query = "SELECT * FROM user WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result


@classmethod
def delete(cls,formulario):
    query = "DELETE * FROM user WHERE id = %(id)s"
    result = connectToMySQL('cannaturals').query_db(query,formulario)
    return result