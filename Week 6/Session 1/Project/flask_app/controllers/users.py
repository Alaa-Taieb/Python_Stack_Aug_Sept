
from flask_app import app
from flask_app.models.user import User
from flask import render_template , request, redirect

@app.route('/')
def log_reg():
    return render_template('main_page.html')


@app.route('/register', methods = ['POST'])
def register():
    data = request.form
    print(data)
    if User.validate_register(data):
        User.create(data)
    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        print("CORRECT!!!")
        return redirect("/dashboard")
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    return "Successful Login!"