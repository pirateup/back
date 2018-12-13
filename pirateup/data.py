from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import WKBElement
from geoalchemy2 import functions as geofunc

db = SQLAlchemy()


class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)


    @classmethod
    def get_or_404(cls, id):
        return cls.query.get_or_404(id)

    def write(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

def query_to_list(query, include_field_names=True):
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)


def extract_field(rec, col):
    field = getattr(rec, col, None)
    if type(field) is WKBElement:
        return db.session.scalar(geofunc.ST_AsGeoJSON(field)) 
    else:
        return field 


def obj_to_list(sa_obj, field_order):
    return [extract_field(sa_obj, field_name) for field_name in field_order]

