from flask_app.config.connectToMySQL import connectToMySQL, DB
from flask_bcrypt import Bcrypt 
from flask_app import app
from flask import flash
import re

bcrypt = Bcrypt(app)


class User:

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            user = cls(result[0])
            return user
        return False
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            user = cls(result[0])
            return user
        return False
    
    @classmethod 
    def register(cls, data):
        data = dict(data)
        data['password'] = bcrypt.generate_password_hash(data['password'])
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def login_validation(cls , data):
        user = cls.get_by_email(data)
        is_valid = True
        if not(user):
            is_valid = False
            flash("User not found with this email.")
        elif not(bcrypt.check_password_hash(user.password , data['password'])):
            is_valid = False
            flash("Wrong password.")

        return is_valid
    
    @classmethod
    def register_validation(cls , data):
        is_valid = True
        user = cls.get_by_email(data)


        if not(cls.EMAIL_REGEX.match(data['email'])) or (user):
            flash("Invalid Email.")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("Invalid FirstName.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Invalid LastName.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords not matching.")
            is_valid = False

        return is_valid
    

