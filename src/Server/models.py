from database import db

class DepotModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)
    items = db.relationship('ItemModel',backref='depot_model',lazy= True)
    def __repr__(self) -> str:
        return f"{self.id}({self.x},{self.y},{self.z})"
    
    def serialize(self, include_inventory = False):
        if include_inventory:
            return {"id" : self.id,"location" : {"x" :self.x,"y" :self.y,"z" :self.z}, "inventory": [item.serialize() for item in self.items]}
        else:
            return {"id" : self.id,"location" : {"x" :self.x,"y" :self.y,"z" :self.z}}


class ItemModel(db.Model):
    item_id = db.Column(db.Integer, primary_key = True)
    depot = db.Column(db.Integer, db.ForeignKey('depot_model.id'), nullable= False)
    name = db.Column(db.String(80))
    count = db.Column(db.Integer)

    def serialize(self):
        return {"name": self.name, "count" : self.count}