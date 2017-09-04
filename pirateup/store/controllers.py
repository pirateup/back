from pirateup.store.models import Store, StoreTag
from pirateup.data import query_to_list
from flask import Flask, request, jsonify, Blueprint
from flask import current_app as app
from geoalchemy2 import functions as geofunc
import geopy

store = Blueprint("store", __name__)


@store.route('/shops', methods=['GET','POST'])
def stores():
    data = request.get_json()
    app.logger.debug(data)
    result = {}
    if request.method == 'POST':
        #ADD NEW STORE
        city = data.get("city")
        street = data.get("street")
        geolocator = geopy.Nominatim() # OpenStreetMaps client
        location = geolocator.geocode("{}, {}".format(street, city))
        data.update({"location": "POINT({} {})".format(location.latitude, location.longitude)})
        store = Store.create(**data)
        return '', 204
    elif request.method == 'GET':
        #RETURN ALL STORES
        app.logger.debug(request.args)
        if 'name' in request.args:
            search_name = request.args.get('name')
            query = Store.query.filter(Store.name.like("%{}%".format(search_name)))
            res = [r for r in query_to_list(query)]
            return jsonify(status='OK',data=res)
        elif 'tag' in request.args:
            search_tag = request.args.getlist('tag')
            app.logger.debug(search_tag)
            query = Store.query.filter(Store.tags.any(StoreTag.name.in_(search_tag)))
            res = [r for r in query_to_list(query)]
            app.logger.debug(res)
            return jsonify(status='OK',data=res)
    return '', 400 


@store.route('/nearby/<point>', methods=['GET'])
@store.route('/nearby/<point>/<int:distance>', methods=['GET'])
def nearby(point, distance=5000):
    """e.g. /nearby/point(54.3733221 18.6257988) 
    or with distance /nearby/point(54.3733221 18.6257988)/3000"""
    query = Store.query.filter(geofunc.ST_Distance(point, Store.location) <= distance)
    res = [r for r in query_to_list(query)]
    app.logger.debug(res)
    app.logger.debug('distance: %s' % distance)
    return jsonify(status='OK',data=res)
