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
        self.users_who_liked = []
        self.user_ids_who_liked = []


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
                SELECT * FROM reviews JOIN users AS creators on reviews.user_id = creators.id
                LEFT JOIN users_liked_reviews ON reviews.id = users_liked_reviews.reviews_id
                LEFT JOIN users AS users_who_liked ON users_liked_reviews.users_id = users_who_liked.id
                ORDER BY reviews.id;
            """
        results = connectToMySQL(DB).query_db(query)
        reviews = []
        
        for row in results:
            # Consider this row to be a new review.
            new_review = True

            # Parse the data of the user that liked the review to a dictionary
            user_who_liked_data = {
                'id': row['users_who_liked.id'],
                'email': results[0]['users_who_liked.email'],
                'fullname': results[0]['users_who_liked.fullname'],
                'password': results[0]['users_who_liked.password'],
                'created_at': results[0]['users_who_liked.created_at'],
                'updated_at': results[0]['users_who_liked.updated_at'],
            }

            # Storing the number of reviews added to the final list.
            number_of_reviews = len(reviews)
            # We are checking if we are on the first iteration of the loop.
            if number_of_reviews > 0:
                # Get the review of the last iteration
                last_review = reviews[number_of_reviews - 1]
                if last_review.id == row['id']:
                    # Appending the user that liked to the last review's
                    last_review.users_who_liked.append(User(user_who_liked_data))

                    last_review.user_ids_who_liked.append(row['users_who_liked.id'])
                    new_review = False
            
            if new_review:
                # Creating an instance of the review
                review = cls(row)

                # Dictionary to create the user who created the review
                creator_dict = {
                    'id': results[0]['creators.id'],
                    'email': results[0]['email'],
                    'fullname': results[0]['fullname'],
                    'password': results[0]['password'],
                    'created_at': results[0]['creators.created_at'],
                    'updated_at': results[0]['creators.updated_at'],
                }

                review.user = User(creator_dict)
                if row['users_who_liked.id']:
                    review.users_who_liked.append(User(user_who_liked_data))
                    review.user_ids_who_liked.append(row['users_who_liked.id'])
                reviews.append(review)
                
        
        # for review in reviews:
        #     print(f"Movie Name: {review.title}")
        #     print(f"Creator: {review.user.fullname}")
        #     for user in review.users_who_liked:
        #         print(f"ID: {user.id}")
        #         print(f"Fullname: {user.fullname}")
        
        
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
    
    @classmethod 
    def add_user_like(cls, data):
        query = "INSERT INTO users_liked_reviews (users_id, reviews_id) VALUES (%(users_id)s, %(reviews_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    @classmethod
    def remove_user_like(cls , data):
        query = "DELETE FROM users_liked_reviews WHERE users_id = %(users_id)s AND reviews_id = %(reviews_id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result

    
