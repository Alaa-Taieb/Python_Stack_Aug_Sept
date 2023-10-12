from flask_app.models.user import User
from flask_app.config.connectToMySQL import connectToMySQL, DB

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
    
        recipe = None

        if result:
            user_data = {
                'id': result[0]['users.id'],
                'first_name': result[0]['first_name'],
                'last_name': result[0]['last_name'],
                'email': result[0]['email'],
                'password': result[0]['password'],
                'created_at': result[0]['users.created_at'],
                'updated_at': result[0]['users.updated_at']
            }
            recipe = cls(result[0])
            recipe.user = User(user_data)
        return recipe
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        result = connectToMySQL(DB).query_db(query)

        recipes = []

        if result:
            for row in result:
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                recipe = cls(row)
                recipe.user = User(user_data)
                recipes.append(recipe)

        return recipes

    @classmethod
    def create(cls , data):
        query = "INSERT INTO recipes (name , description, instructions, date, under_30, user_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(date)s,%(under_30)s, %(user_id)s);"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        return result