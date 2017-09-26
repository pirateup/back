from flask import Flask, request, jsonify
from .data import db
from .store.controllers import store
from flask_json import FlaskJSON
import os
import requests

app = Flask(__name__)
json = FlaskJSON(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(store)

@app.route('/')
def hello_world():
    return 'Hello, World!'


