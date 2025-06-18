from flask import Blueprint, jsonify, make_response
from flask_restful import Resource # Import Resource from flask_restful for API endpoints
from server.config import db, api
from server.models.restaurant import Restaurant # Import the Restaurant model

# Create a Blueprint for restaurant routes
restaurant_bp = Blueprint('restaurant_bp', __name__)

class RestaurantList(Resource):
    def get(self):
        """
        Handles GET request for /restaurants.
        Returns a list of all restaurants.
        """
        restaurants = Restaurant.query.all()
        # Serialize each restaurant using the serialize method which does not include pizzas
        serialized_restaurants = [restaurant.serialize() for restaurant in restaurants]
        return make_response(jsonify(serialized_restaurants), 200)

class RestaurantById(Resource):
    def get(self, id):
        """
        Handles GET request for /restaurants/<int:id>.
        Returns details of a single restaurant and its pizzas.
        """
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        # Serialize the restaurant using the to_dict method which includes pizzas
        return make_response(jsonify(restaurant.to_dict()), 200)

    def delete(self, id):
        """
        Handles DELETE request for /restaurants/<int:id>.
        Deletes a restaurant and all related RestaurantPizzas due to cascading delete.
        """
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)

        db.session.delete(restaurant)
        db.session.commit()
        # Return 204 No Content on successful deletion
        return make_response("", 204) # Empty response body

# Add the resources to the API
api.add_resource(RestaurantList, '/restaurants')
api.add_resource(RestaurantById, '/restaurants/<int:id>')