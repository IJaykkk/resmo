# 3rd party
from flask import abort, request, jsonify, g

# local
from service import app, auth, db
from service.models.user import User
