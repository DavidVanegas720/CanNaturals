
from Flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import jsonify

class Users:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('proyecto_grupal').query_db(query, formulario)
        return result
    
    @classmethod
    def get_user_by_id(cls,formulario):
        query = "SELECT * FROM user WHERE id = %(id)s"
        result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
        return result


    @classmethod
    def delete(cls,formulario):
        query = "DELETE * FROM user WHERE id = %(id)s"
        result = connectToMySQL('proyecto_grupal').query_db(query,formulario)
        return result


    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('proyecto_grupal').query_db(query, formulario)
        return result
