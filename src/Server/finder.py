from flask import request
from flask_restful import Resource, abort
from database import db
from models import ItemModel

class ItemFinder(Resource):
    def post(self):
        item_to_find = request.json
        print(item_to_find)
        res ={}
        for name in item_to_find:
            print(name)
            items = ItemModel.query.filter_by(name= name)
            if len(items.all()) == 0:
                abort(404)
            else:
                res[name] = {}
                for item in items:
                    res[item.name][item.depot] = item.count
                
        return res