"""
Package: app

Package for the application models and services
This module also sets up the logging to be used with gunicorn
"""

from flask import Flask
from flask_restful import Resource, Api

# Create Flask application
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
