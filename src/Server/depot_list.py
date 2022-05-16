from ast import dump
from itertools import count
from webbrowser import get
from flask_restful import Resource, abort, reqparse
from database import db
from models import DepotModel, ItemModel
from flask import Blueprint, request
from json import dumps, loads

depots = Blueprint("depots", __name__, static_folder="static",
                   template_folder="templates")

parser = reqparse.RequestParser()
parser.add_argument("id", type=int, help="Unique Depot ID")
parser.add_argument("location_x", type=int, help="X coordinate of the Depot")
parser.add_argument("location_y", type=int, help="y coordinate of the Depot")
parser.add_argument("location_z", type=int, help="z coordinate of the Depot")


class DepotList(Resource):
    def get(self):
        entries = [entry.serialize() for entry in DepotModel.query.all()]
        return entries
    def post(self):
        args = parser.parse_args()
        depot = DepotModel(x = args["location_x"],y = args["location_y"],z = args["location_z"])
        db.session.add(depot)
        db.session.commit()
        return(depot.serialize())
class Depot(Resource):
    def get(self,id):
        depot =DepotModel.query.filter_by(id=id).first_or_404()
        return [item.serialize() for item in depot.items]
    def delete(self,id):
        depot =DepotModel.query.filter_by(id=id).first_or_404()
        db.session.delete(depot)
        db.session.commit()
        return {"result" : "success"},200
class Item(Resource):
    def put(self,id):
        DepotModel.query.filter_by(id=id).first_or_404()
        itemdict = request.json
        for key in itemdict:
            item = ItemModel.query.filter_by(depot= id,name=key).first()
            if item is not None:
                print(f"Found existing item {item}")
                item.count = itemdict[key]
                db.session.commit()
            else:
                item = ItemModel(depot= id,name= key, count= itemdict[key])
                db.session.add(item)
                db.session.commit()