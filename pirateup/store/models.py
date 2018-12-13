from pirateup.data import db, CRUDMixin 
from geoalchemy2 import Geography

store_tags = db.Table('store_tag_rel',
        db.Column('store_id', db.Integer, db.ForeignKey('store.id')),
        db.Column('tag_id', db.Integer, db.ForeignKey('store_tag.id')))

class Store(db.Model, CRUDMixin):
    __tablename__ = 'store'

    name = db.Column(db.String())
    city = db.Column(db.String())
    street = db.Column(db.String())
    zip = db.Column(db.String())
    location = db.Column(Geography(geometry_type='POINT',srid=4326))
    tags = db.relationship('StoreTag', secondary=store_tags, 
            backref=db.backref('stores', lazy='dynamic'))


class StoreTag(db.Model, CRUDMixin):
    __tablename__ = 'store_tag'

    name = db.Column(db.String())
