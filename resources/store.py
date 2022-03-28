__author__ = "Himmler Louissaint"

from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'store': store.json()}, 200
        return {'message': f'Store {name} not found.'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f"Store {name} already exists."}, 400
        store = StoreModel(name)
        try:
            store.save()
        except:
            return {'message': f'An error has occurred while creating store {name}.'}, 500
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete()
            except Exception as e:
                return {'message': f'An error has occurred while deleting store {name}... Error msg: {e}'}, 500
        return {'message': f'{name} has been deleted.'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}