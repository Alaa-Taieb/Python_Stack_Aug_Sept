from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models.burger import Burger

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.quantity = data['quantity']
        self.order_date = data['order_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burger = None

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burger_id WHERE orders.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        order = None
        if result != []:
            
            burger_data = {
                'id': result[0]['burgers.id'],
                'name': result[0]['name'],
                'bun': result[0]['bun'],
                'meat': result[0]['meat'],
                'calories': result[0]['calories'],
                'created_at': result[0]['burgers.created_at'],
                'updated_at': result[0]['burgers.updated_at']
            }
            burger = Burger(burger_data)
            order = cls(result[0])
            order.burger = burger
        return order
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burger_id;"
        results = connectToMySQL(DB).query_db(query)

        orders = []
        if results != []:
            for item in results:
                order = cls(item)

                burger_data = {
                    'id': item['burger.id'],
                    'name': item['name'],
                    'bun': item['bun'],
                    'meat': item['meat'],
                    'calories': item['calories'],
                    'created_at': item['burgers.created_at'],
                    'updated_at': item['burgers.updated_at']
                }
                order.burger = Burger(burger_data)
                orders.append(order)
        return orders
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO orders (customer_name, quantity, order_date, burger_id) values(%(customer_name)s , %(quantity)s ,%(order_date)s , %(burger_id)s);"
        return connectToMySQL(DB).query_db(query , data)

    @classmethod 
    def delete(cls , data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET customer_name=%(customer_name)s, quantity=%(quantity)s, order_data=%(order_data)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)

    @classmethod 
    def get_orders_by_burger(cls , data):
        query = "SELECT * FROM orders WHERE burger_id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        orders = []
        for item in results:
            order = cls(item)
            orders.append(order)
        return orders