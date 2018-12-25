from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'items':self.items}



    @classmethod
    def find_item_by_name(cls, name):
        return ItemModel.query.filter_by(name = name).first() # select * from items where name = name, LIMIT=1

    def save_to_db(self):        # Does insert and update both
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
