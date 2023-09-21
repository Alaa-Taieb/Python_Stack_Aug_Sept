from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.burger import Burger
from flask_app.models.order import Order

@app.route('/')
def home():
    burgers = Burger.get_all()
    Order.get_by_id({'id': 1})
    return render_template('index.html', burgers = burgers)

@app.route('/burgers', methods=['POST'])
def create_post():
    Burger.create(request.form)
    return redirect('/')

@app.route('/burger/<int:id>')
def burger_details(id):
    data = {'id': id}
    burger = Burger.get_one(data)

    orders = Order.get_orders_by_burger(data)
    return render_template('burger.html', burger = burger , orders = orders)

@app.route('/delete/<int:id>')
def burger_delete(id):
    data = {'id': id}
    Burger.delete(data)
    return redirect('/')

@app.route('/burger/update', methods=['POST'])
def burger_update():
    data = request.form
    Burger.update(data)
    return redirect(f"/burger/{data['id']}")

@app.route('/burger/<int:id>/order')
def order_burger(id):
    return render_template('create_order.html' , burger_id = id)

@app.route('/order/create' , methods=['POST'])
def create_order():
    data = request.form
    Order.create(data)
    return redirect(f"/burger/{data['burger_id']}")