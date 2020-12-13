from datetime import timedelta

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authentication, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

# If we want to change the url to the authentication endpoint instead of default /auth
# app.config['JWT_AUTH_URL_RULE'] = '/login'

# the authentication endpoint (by default, /auth );
jwt = JWT(app, authentication, identity)

# config JWT Token Expiration within half an hour, instead of default 5 min
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

# config JWT Authentication key name to be 'email' instead of default 'username'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({'access_token': access_token.decode('utf-8'),
                    'user_id': identity.id
                    })

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

'''__name__ is a built-in variable which evaluates to the name of the current module.
Thus it can be used to check whether the current script is being run on its own or
being imported somewhere else by combining it with if statement, as shown below.
'''
if __name__ == '__main__':
    app.run(port=5000, debug=True)

