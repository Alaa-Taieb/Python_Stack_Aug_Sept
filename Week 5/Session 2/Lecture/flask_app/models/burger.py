from flask_app.config.mysqlconnection import connectToMySQL, DB

class Burger:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL(DB).query_db(query)
        burgers = []
        for item in results:
            """"
            item = {
                'id': 1
                'name': 'burger 1',
                'bun': 'bun 1',
                'meat': 'meat 1',
                'calories': 450,
                'created_at': '2023-09-19 19:50:42',
                'updated_at': '2023-09-19 19:50:42'
            }
            """
            burger = cls(item)
            burgers.append(burger)
        return burgers
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM burgers WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        burger = None
        if result != []:
            burger = cls(result[0])
        return burger
    

    @classmethod
    def create(cls, data):

        """"
        data = {
            'name': 'burger 1',
            'bun': 'bun 1',
            'meat': 'meat 1',
            'calories': '450'
        }
        """

        query = "INSERT INTO burgers (name , bun , meat , calories) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s)"
        return connectToMySQL(DB).query_db(query , data)

    @classmethod
    def delete(cls , data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)

    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
