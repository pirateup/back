from pirateup.data import db, CRUDMixin 
from geoalchemy2 import Geography

class Store(db.Model, CRUDMixin):
    __tablename__ = 'store'

    name = db.Column(db.String())
    city = db.Column(db.String())
    street = db.Column(db.String())
    zip = db.Column(db.String())
    location = db.Column(Geography(geometry_type='POINT',srid=4326))
