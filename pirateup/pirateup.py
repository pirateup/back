from flask import Flask
from pirateup.store.models import Store
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return 'Hello, World!'
