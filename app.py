from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Turns off Flask tracker not SQLALchemy Tracker
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(UserRegister,'/register')

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__': #Python executes statements in of a imported file; to prevent some statement to execute when imported do this
    from db import db  #importing here due to circular import problem
    db.init_app(app)
    app.run(port=5000, debug = True)
