from flask import Flask
from flask_restful import Api
from database import db
from depot import Depot
from depot_list import DepotList
from finder import ItemFinder

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.add_resource(DepotList, "/depots/")
api.add_resource(ItemFinder, "/find/")
api.add_resource(Depot, "/depot/<int:id>/")
db.app = app
db.init_app(app)

if(__name__ == "__main__"):
    app.run(debug=True)
