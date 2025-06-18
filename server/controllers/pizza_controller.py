from flask import Blueprint, jsonify, make_response
from flask_restful import Resource # Import Resource from flask_restful
from server.config import db, api
from server.models.pizza import Pizza # Import the Pizza model

# Create a Blueprint for pizza routes
pizza_bp = Blueprint('pizza_bp', __name__)

class PizzaList(Resource):
    def get(self):
        """
        Handles GET request for /pizzas.
        Returns a list of all pizzas.
        """
        pizzas = Pizza.query.all()
        serialized_pizzas = [pizza.serialize() for pizza in pizzas]
        return make_response(jsonify(serialized_pizzas), 200)

# Add the resource to the API
api.add_resource(PizzaList, '/pizzas')