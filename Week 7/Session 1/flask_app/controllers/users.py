
from flask_app import app
from flask_app.models.user import User
from flask_app.models.review import Review
from flask import render_template , request, redirect, session

@app.route('/')
def log_reg():
    if 'user_id' in session:
        return redirect('/dashboard')

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
        user = User.get_by_email(data)
        print("CORRECT!!!")
        session["user_id"] = user.id
        return redirect("/dashboard")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')

    reviews = Review.get_all()
    user = User.get_by_id({'id': session['user_id']})
    print(f"Type: {type(user.id)}")


    return render_template("dashboard.html", logged_user = user, reviews = reviews)