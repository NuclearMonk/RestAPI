from flask_restful import Resource
from database import db
from models import DepotModel

class DepotList(Resource):
    def get(self):
        entries = [entry.serialize() for entry in DepotModel.query.all()]
        return entries

    def post(self):
        args = request.json
        depot = DepotModel( x=args["location"]["x"],
                            y=args["location"]["y"],
                            z=args["location"]["z"])
        db.session.add(depot)
        db.session.commit()
        return(depot.serialize())



