from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.burger import Burger

@app.route('/')
def home():
    burgers = Burger.get_all()
    return render_template('index.html', burgers = burgers)

@app.route('/burgers', methods=['POST'])
def create_post():
    Burger.create(request.form)
    return redirect('/')

@app.route('/details/<int:id>')
def burger_details(id):
    data = {'id': id}
    burger = Burger.get_one(data)
    return render_template('burger.html', burger = burger)

@app.route('/delete/<int:id>')
def burger_delete(id):
    data = {'id': id}
    Burger.delete(data)
    return redirect('/')