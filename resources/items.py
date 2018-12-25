import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel




class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required = True,
    help = 'This field cannot be blank')

    @jwt_required()
    def get(self, name):
        result = ItemModel.find_item_by_name(name)
        if result:
            return result.json()
        return {'message': 'Item not found'}, 404


    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'message': "The item '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item'}, 500

        return item.json() , 201


    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message' : 'item Deleted'}

    def put(self, name):
        data = request.get_json
        item = ItemModel.find_item_by_name(name)

        if item is None:
            try:
                item = ItemModel(name, data['price'])
            except:
                return {'message': 'An error occured inserting the item'}, 500

        else:
            try:
                item.price = data['price']
            except:
                return {'message': 'An error occured updating the item'}, 500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items' : list(map(lambda x : x.json(), ItemModel.query.all()))}
