import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = 'This field cannot be blank')

    parser.add_argument('password',
    type = str,
    required = True,
    help = 'This field cannot be blank')

    parser.add_argument('email',
    type = str,
    help = 'This field cannot be blank')


    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_user_name(data['username']):
            return {"message": "A user with that username already exists"}, 300

        user = UserModel(data['username'], data['password'], data['email'])
        user.save_to_db()

        return {'message' : 'user created successfully'}, 201

class Users(Resource):
    def get(self):
        return {'users' : list(map(lambda x : x.json(), UserModel.query.all()))}
