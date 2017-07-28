from pirateup.data import db, CRUDMixin 

class Store(db.Model, CRUDMixin):

    name = db.Column(db.String())
