'''
Defines custom Flask Blueprint for the /api/ resource prefix & all subroutes
'''

from flask import Blueprint
from flask_restful import Api
from resources.requests import Requests

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Requests, '/requests')