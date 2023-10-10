from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Event:
    db_name = "ajax_demo"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events"

        results = connectToMySQL(cls.db_name).query_db(query)
        all_posts = []
        for result in results:
            all_posts.append(cls(result))
        return all_posts

    @classmethod
    def add(cls, data):
        query=  "INSERT INTO events(title) "\
                "VALUES(%(title)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def reset(cls):
        query = "DELETE FROM events"
        return connectToMySQL(cls.db_name).query_db(query)
