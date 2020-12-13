import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.utilities import Utilities as util

# Creating Item Resource to connect/interact with client (POSTMAN) server
class Item(Resource):

    def __init__(self):
        pass

    parse = reqparse.RequestParser()
    parse.add_argument('price',
                       type=float,
                       required=True,
                       help='This Field Cannot Be Blank: '
                       )

    def get(self, name):
        item = util.find_by_name(name)
        if item:
            return item
        return {"Message": "Item not found "}

    def post(self, name):

        if util.find_by_name(name):
            return {'message':'{} Already Exist in Table' .format(name)}

        data = Item.parse.parse_args()
        item = {'name': name,
                'price': data['price']
                }
        try:
            util.insert(item)
        except:
            return {'Message': "An error occured inseting the item '{}'".format(item)}, 500

        return item, 201

    def delete(self, name):

        conn, cursor = util.db_connection()

        if util.find_by_name(name):
            delete_query = "DELETE FROM items Where name = ?"
            # cursor.execute(delete_query, (item['name'],))
            cursor.execute(delete_query, (name,))

            conn.commit()
            conn.close()
            return {'message': "'{}' Item Deleted".format(name)}
        else:
            return {'items': "'{}' Item not Exist".format(name)}, 404

    def put(self, name):

        conn, cursor = util.db_connection()

        data = Item.parse.parse_args()
        item = {'name': name,
                'price': data['price']
                }
        if util.find_by_name(name) is None:
            try:
                util.insert(item)
            except:
                return {'Message': "An error occur inserting the item '{}'".format(item)}, 500
        else:
            try:
                util.update(item)
            except:
                return {'Message': "An error occur updating the item '{}'".format(item)}, 500

        return item


# creating Class for List of Items to be requested
class ItemList(Resource):
    @jwt_required()
    def get(self):
        conn, cursor = util.db_connection()
        select_query = "SELECT * FROM items"
        result = cursor.execute(select_query)
        row = result.fetchall()

        if row:
            items = []
            for data in row:
                print(data)
                items.append({'name': data[0], 'price': data[1]})

            conn.close()
            return {'ItemList': items}
        return {'Message': "Items not found"}
