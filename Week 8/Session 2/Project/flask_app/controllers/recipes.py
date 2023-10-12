from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

from flask import session, redirect, render_template, request


@app.route("/dashboard")
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id': session['user_id']})
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user = logged_user , recipes = recipes)

@app.route('/recipe/create')
def create():
    if not 'user_id' in session:
        return redirect('/')
    
    return render_template("create_recipe.html")

@app.route('/recipe/add', methods=['POST'])
def add_recipe():
    data = request.form
    Recipe.create(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>/edit')
def update(id):
    if not 'user_id' in session:
        return redirect('/')
    
    recipe = Recipe.get_by_id({'id': id})
    if session['user_id'] != recipe.user.id:
        return redirect('/dashboard')
    return render_template("update_recipe.html",recipe = recipe)

@app.route('/recipe/edit', methods=['POST'])
def edit_recipe():
    data = request.form
    Recipe.edit(data)
    return redirect('/dashboard')

@app.route("/recipe/<int:id>")
def view(id):
    if not 'user_id' in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id': session['user_id']})
    recipe = Recipe.get_by_id({'id': id})

    return render_template("view_recipe.html" , recipe = recipe, user = logged_user)

@app.route("/recipe/<int:id>/delete")
def delete(id):
    if not 'user_id' in session:
        return redirect('/')
    
    Recipe.delete({'id': id})
    return redirect("/dashboard")