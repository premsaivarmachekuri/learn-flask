from flask import Flask, send_from_directory, abort
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False 

@app.route("/")
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route("/about/")
def about():
    return '<h1>This is a Flask Application</h1>'

ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '  # Example allowed characters
@app.route('/capitalize/<string:word>/')
def cap(word):
    if not all(char in ALLOWED_CHARS for char in word):
        return 'Invalid characters in input!', 400  # Return error for invalid input
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return '<h1>{} + {} = {}</h1>'.format(a,b,a+b)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9000')
