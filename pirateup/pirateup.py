from flask import Flask, request, jsonify
from pirateup.store.models import Store
from .data import db
import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/shops', methods=['GET','POST'])
def stores():
    data = request.get_json()
    print(data)
    result = {}
    if request.method == 'POST':
        #ADD NEW STORE
        store = Store.create(**data)
        result = {'status': 'OK'}        
    elif request.method == 'GET':
        #RETURN ALL STORES
        pass

    return jsonify(status='OK'), 200 
