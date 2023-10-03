from flask_app import app
from flask_app.models.review import Review
from flask_app.models.user import User


from flask import request, render_template, session, redirect

@app.route('/review/add-review')
def add_review():
    user = User.get_by_id({'id': session['user_id']})
    return render_template("add_review.html", logged_user = user)

@app.route('/review/create' , methods=['POST'])
def create():
    Review.create(request.form)
    return redirect('/dashboard')

@app.route('/review/<int:id>/edit')
def edit_review(id):
    review = Review.get_by_id({'id': id})
    if review.user.id != session['user_id']:
        return redirect('/dashboard')
    return render_template('edit_review.html', review = review)


@app.route('/review/update', methods=['POST'])
def update():
    print("*"*100)
    print(session['user_id'])
    if int(request.form['user_id']) == int(session['user_id']):
        print("We are IN!!!!")
        Review.update(request.form)
    return redirect('/dashboard')

@app.route('/review/<int:id>/delete')
def delete(id):
    review = Review.get_by_id({'id': id})
    
    if review.user.id == session['user_id']:
        
        Review.delete({'id': id})
    return redirect('/dashboard')

@app.route('/review/<int:id>')
def show_review(id):
    review = Review.get_by_id({'id': id})
    return render_template("show_review.html", review = review)

@app.route('/review/<int:id>/like')
def like(id):
    Review.add_user_like({'users_id': session['user_id'] , 'reviews_id': id})
    return redirect('/dashboard')

@app.route('/review/<int:id>/dislike')
def dislike(id):
    print({'users_id': session['user_id'] , 'reviews_id': id})
    Review.remove_user_like({'users_id': session['user_id'] , 'reviews_id': id})
    return redirect('/dashboard')