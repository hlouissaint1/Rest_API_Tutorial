__author__ = "Himmler Louissaint"
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

class UserList(Resource):
#    @jwt_required()
    def get(self):
        return {'users': [user.json() for user in UserModel.find_all()]}


class UserInfo(Resource):
#    @jwt_required()
    def get(self, username):
        user = UserModel.find_by_username(username)
        return ({'user': user.json()}, 200) if user else ({'message': f'User {username} not found.'}, 404)


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This username field cannot be empty.")
    parser.add_argument('password', type=str, required=True, help="This username field cannot be empty.")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": f"User {data['username']} already exists in our database."}, 400
        user = UserModel(**data)
        user.save()
        return {"message": f"User {data['username']} is successfully registered."}, 201






