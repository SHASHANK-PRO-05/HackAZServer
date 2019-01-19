from flask import Flask, render_template, redirect, url_for, request, jsonify
import jwt
import json

with open('./config.json', 'r') as f:
    config = json.load(f)

secret_key = config['SERVER_KEY']

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        age = request.form['age']
        tags = request.form['tags']
        expertise = request.form['expertise']
    else:
        email = request.args['email']
        password = request.args['password']
        name = request.form['name']
        phone = request.form['phone']
        age = request.form['age']
        tags = request.form['tags']
        expertise = request.form['expertise']

    #TODO Save to database


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    else:
        email = request.args['email']
        password = request.args['password']

    # Create an authentication token
    encoded = jwt.encode({'email': email, 'password':password}, secret_key, algorithm='HS256')

    # Convert byte to string
    encoded = encoded.decode('utf-8')

    #TODO jsonify
    return encoded


@app.route('/otherapi', methods=['GET', 'POST'])
def otherapi():
    error = None
    if request.method == 'POST':
        header = request.headers['authorization']
        bearer = header.split(' ')
        token = bearer[1]
        user_cred_dict = jwt.decode(token, secret_key)

    #TODO incomplete


    return render_template('login.html', error=error)



if __name__ == '__main__':
    app.debug()
