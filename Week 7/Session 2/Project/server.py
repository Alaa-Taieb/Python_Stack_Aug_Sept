from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def index():
    request = requests.get('https://restcountries.com/v3.1/all?fields=name,flags')
    data = request.json()

    return render_template("index.html", countries = data)

@app.route('/get_all_apis')
def api_entries():
    request = requests.get('https://api.publicapis.org/entries')
    data = request.json()['entries']
    return render_template('apis_list.html', entries = data)




if __name__ == "__main__":
    app.run(debug = True)