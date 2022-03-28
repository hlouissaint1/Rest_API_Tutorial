__author__ = "Himmler Louissaint"

from flask_restful import Resource, reqparse
from models.item import ItemModel
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be empty")
    parser.add_argument('stores_id', type=int, required=True, help="Every item needs a store id")


#    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        return ({'item': item.json()}, 200) if item else ({'message': f'{name} is not found.'}, 404)

    def post(self, name):
        if ItemModel.find_by_name(name):
            return  {'message': f"{name} already exists."}, 400
        data = Item.parser.parse_args()
#        item = ItemModel(name, **data)
        item = ItemModel(name, data['price'], data['stores_id'])
        try:
            item.save()
            return {'message': f'{name} has been successfully saved.'}
        except:
            return {'message': f'Error while saving {name}.'}


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save()
        return item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
        return {'message': f'{name} has been successfully deleted.'}


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}


