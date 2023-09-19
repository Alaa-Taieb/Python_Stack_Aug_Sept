from flask import Flask, render_template, request,redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/options' , methods=['POST'])
def options():
    print('-'*50)
    print(request.form)
    return request.form

if __name__ == "__main__":
    app.run(debug=True)