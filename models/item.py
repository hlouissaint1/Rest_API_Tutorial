__author__ = "Himmler Louissaint"

from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    stores_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    def __init__(self, name, price, stores_id):
        self.name = name
        self.price = price
        self.stores_id = stores_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'stores_id': self.stores_id}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        print(self.id)

    def delete(self):
        db.session.delete(self)
        db.commit()


if __name__ == '__main__':
    name = 'piano'
    item = ItemModel('saxophone', 1299, 1)
    print(item.json())
    db.session.add(item)
 #   db.session.commit()
