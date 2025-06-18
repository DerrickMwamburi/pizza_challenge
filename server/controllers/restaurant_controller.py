from flask import Blueprint, jsonify, make_response
from flask_restful import Resource
from server.config import db, api
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__)

class RestaurantList(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        serialized_restaurants = [restaurant.serialize() for restaurant in restaurants]
        return make_response(jsonify(serialized_restaurants), 200)

class RestaurantById(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        return make_response(jsonify(restaurant.to_dict()), 200)

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)

        db.session.delete(restaurant)
        db.session.commit()
        return make_response("", 204)
    
api.add_resource(RestaurantList, '/restaurants')
api.add_resource(RestaurantById, '/restaurants/<int:id>')