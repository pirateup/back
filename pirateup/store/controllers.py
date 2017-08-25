from pirateup.store.models import Store
from pirateup.data import query_to_list
from flask import Flask, request, jsonify, Blueprint
from flask import current_app as app

store = Blueprint("store", __name__)


@store.route('/shops', methods=['GET','POST'])
def stores():
    data = request.get_json()
    app.logger.debug(data)
    result = {}
    if request.method == 'POST':
        #ADD NEW STORE
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
            #for r in res:
            #    app.logger.debug(r)
    return '', 400 
