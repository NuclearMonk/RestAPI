from flask import request
from flask_restful import Resource
from database import db

from models import DepotModel, ItemModel


class Depot(Resource):
    def get(self, id):
        
        depot = DepotModel.query.filter_by(id=id).first_or_404()
        return depot.serialize(include_inventory = True)

    def delete(self, id):
        depot = DepotModel.query.filter_by(id=id).first_or_404()
        db.session.delete(depot)
        db.session.commit()
        return {"result": "success"}, 200

    def put(self, id):
        DepotModel.query.filter_by(id=id).first_or_404()
        items_to_update = request.json
        for item in items_to_update:
            db_item = ItemModel.query.filter_by(depot=id, name=item).first()
            if db_item is not None:
                count = items_to_update[item]
                if(count == 0):
                    db.session.delete(db_item)
                else:
                    db_item.count = items_to_update[item]
                db.session.commit()
            else:
                db_item = ItemModel(depot=id, name=item,
                                    count=items_to_update[item])
                db.session.add(db_item)
                db.session.commit()