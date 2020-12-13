import sqlite3
from flask_restful import Resource, reqparse

from models.helper import UserModel

# will get data from POSTMAN and insert into sqlite3 database(users table) for authentication purpose
class UserRegister(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('username',
                       type=str,
                       required=True,
                       help="Username should not be Blank"
                       )
    parse.add_argument('password',
                       type=str,
                       required=True,
                       help="Password should not be Blank"
                       )

# when run POSTMAN POST /register it will call this method through app.pyv
    def post(self):

        data = UserRegister.parse.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"Message": "A user with that username already exists"}, 400

        conn = sqlite3.connect('Api_data.db')
        cursor = conn.cursor()

        insert_query = '''INSERT OR IGNORE INTO users (username, password)
                        VALUES(?,?)'''
        # data['username'], ...... will get value from data = UserRegister.parse.parse_args()
        conn.execute(insert_query, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return {'Message': 'User Register Successfully /users/post'}, 201
