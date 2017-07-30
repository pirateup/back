from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookie = db.Column(db.String, unique=True)

    def __init__(self, cookie):
        self.cookie = cookie

    def __repr__(self):
        return '<User cookie is %d>' % self.cookie