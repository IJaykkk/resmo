""""
Package: app

Package for the application models and services
This module also sets up the logging to be used with gunicorn
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

# Create Flask application
app = Flask(__name__)
# api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from service.controllers import users
from service.controllers import posts
from service.controllers import configs 
