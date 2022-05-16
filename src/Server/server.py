from sys import prefix
from flask import Flask
from flask_restful import Api
from database import db
from depot_list import DepotList,Depot, Item, depots

app = Flask(__name__)
api = Api(app)
app.register_blueprint(depots, prefix="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.add_resource(DepotList, "/depots")
api.add_resource(Item, "/depot/<int:id>/items")
api.add_resource(Depot, "/depot/<int:id>")
db.app = app
db.init_app(app)

if(__name__ == "__main__"):
    app.run(debug=True)
