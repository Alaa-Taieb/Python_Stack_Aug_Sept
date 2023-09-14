from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "sdkfjhejnfsdkufhe"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit_info', methods=['POST'])
def submit():
    # Our inefficient solution
    # if session.get('value_list') == None:
    #     print("Session is empty")
    #     session['value_list'] = []
    
    # print(f"Before: {session.get('value_list')}")
    
    # list = session['value_list']
    # list.append(dict(request.form))
    # session['value_list'] = list

    # print(f"After: {session.get('value_list')}")
    # return redirect('/display_info')

    # ChatGPT's Solution:
    if session.get('value_list') is None:
        print("Session is empty")
        session['value_list'] = []
    
    print(f"Before: {session.get('value_list')}")
    session['value_list'].append(dict(request.form))
    session.modified = True  # Mark the session as modified
    print(f"After: {session.get('value_list')}")
    return redirect('/display_info')

@app.route('/display_info')
def display_info():
    return render_template('info.html' , value_list = session.get('value_list'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)