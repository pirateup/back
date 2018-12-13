from back.pirateup.data import db, CRUDMixin


class User(db.Model, CRUDMixin):
    cookie = db.Column(db.String, unique=True)

    def __init__(self, cookie):
        self.cookie = cookie

    def __repr__(self):
        return '<User cookie is %d>' % self.cookie
