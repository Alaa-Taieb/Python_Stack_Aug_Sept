from flask import redirect, render_template, session, request
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def home():
    if 'user_id' in session:
        return redirect('/dashboard')
    
    return render_template("index.html")

@app.route("/login" , methods=['POST'])
def login():
    data = request.form
    if (User.login_validation(data)):
        user = User.get_by_email(data)
        session['user_id'] = user.id
    return redirect('/')

@app.route("/register", methods = ['POST'])
def register():
    data = request.form
    if (User.register_validation(data)):
        User.register(data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')