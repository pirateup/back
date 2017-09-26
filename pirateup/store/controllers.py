from pirateup.store.models import Store, StoreTag
from pirateup.data import query_to_list
from flask import Flask, request, jsonify, Blueprint
from flask import current_app as app
from geoalchemy2 import functions as geofunc
from flask_json import as_json, json_response
import geopy

store = Blueprint("store", __name__)


def new_store(data):
    #ADD NEW STORE
    city = data.get("city")
    street = data.get("street")
    geolocator = geopy.Nominatim() # OpenStreetMaps client
    location = geolocator.geocode("{}, {}".format(street, city))
    data.update({"location": "POINT({} {})".format(location.latitude, location.longitude)})
    store = Store.create(**data)
    return json_response(status=204)


def query_store_by_name(name):
    query = Store.query.filter(Store.name.like("%{}%".format(name)))
    res = [r for r in query_to_list(query)]
    return dict(data=res)


def query_store_by_tag(tag):
    query = Store.query.filter(Store.tags.any(StoreTag.name.in_(tag)))
    res = [r for r in query_to_list(query)]
    return dict(data=res)



@store.route('/shops', methods=['GET','POST'])
@as_json
def stores():
    data = request.get_json()
    app.logger.debug(data)
    if request.method == 'POST':
        return new_store(data)
    elif request.method == 'GET':
        #RETURN ALL STORES
        app.logger.debug(request.args)
        if 'name' in request.args:
            search_name = request.args.get('name')
            return query_store_by_name(search_name)
        elif 'tag' in request.args:
            search_tag = request.args.getlist('tag')
            return query_store_by_tag(search_tag)
        return json_response(status=400) 


@store.route('/nearby/<point>', methods=['GET'])
@store.route('/nearby/<point>/<int:distance>', methods=['GET'])
def nearby(point, distance=5000):
    """e.g. /nearby/point(54.3733221 18.6257988) 
    or with distance /nearby/point(54.3733221 18.6257988)/3000"""
    query = Store.query.filter(geofunc.ST_Distance(point, Store.location) <= distance)
    res = [r for r in query_to_list(query)]
    app.logger.debug(res)
    app.logger.debug('distance: %s' % distance)
    return dict(data=res)
