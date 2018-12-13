from flask import Flask, request, make_response, jsonify
from .data import db
from .store.controllers import store
from back.pirateup.users.models import User
from flask_json import FlaskJSON
import os
import requests
import string
from random import *

app = Flask(__name__)
json = FlaskJSON(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(store)

@app.route('/')
def hello_world():
    user_cookie = request.cookies.get('user_cookie')
    if user_cookie == None:
        resp = make_response('Hello, World! You now have cookie!')
        # TODO(wojtek): Check if unique=True is good enaugh
        user = User(random_string())
        resp.set_cookie('user_cookie',user.cookie)

        return resp
    else:
        return 'Hello, World! You had cookie ' + user_cookie

def random_string():
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    random_string = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return random_string

if __name__ == '__main__':
    app.run()
