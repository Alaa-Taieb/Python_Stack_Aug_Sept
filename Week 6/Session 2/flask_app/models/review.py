from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.user import User

class Review:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.content = data['content']
        self.date_watched = data['date_watched']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None


    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query , data)

        review = None
        if results:
            user_data = {
                'id': results[0]['users.id'],
                'email': results[0]['email'],
                'fullname': results[0]['fullname'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at'],
            }
            review = cls(results[0])
            review.user = User(user_data)
        return review
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM reviews JOIN users ON reviews.user_id = users.id;
            """
        results = connectToMySQL(DB).query_db(query)
        reviews = []
        if results:
            for row in results:
                user_data = {
                'id': row['users.id'],
                'email': row['email'],
                'fullname': row['fullname'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                }
                review = cls(row)
                review.user = User(user_data)
                reviews.append(review)
        return reviews
    
    @classmethod 
    def create(cls , data):
        query = "INSERT INTO reviews (title , rating, date_watched, content, user_id) VALUES(%(title)s,%(rating)s,%(date_watched)s,%(content)s,%(user_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def update(cls, data):
        query = "UPDATE reviews SET title = %(title)s, rating= %(rating)s, date_watched=%(date_watched)s, content=%(content)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM reviews WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
