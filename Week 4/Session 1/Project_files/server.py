from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/anotherRoute')
def another_route():
    return 'You have hit another route.'

@app.route('/users/<string:username>')
def username(username):
    return f"Welcome {username}"


@app.route('/dashboard/<string:region>')
def dashboard(region):
    print(region)
    article = ""
    if region == 'Tunis':
        region = "Capital City"
        article = "Somthing about tunis bla blal"
    elif region == "Sfax":
        article = "Sfax know for olive oil"
    
    stacks = ['python' , 'web fundamentals', 'C#']
    
    return render_template('index.html', var1 = region, var2 = article, var3 = stacks )

if __name__ == "__main__":
    app.run(debug=True)