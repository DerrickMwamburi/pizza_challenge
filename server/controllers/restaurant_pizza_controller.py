from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource
from server.config import db, api
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant 
from server.models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

class RestaurantPizzaCreate(Resource):
    def post(self):
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not all([price, pizza_id, restaurant_id]):
            return make_response(jsonify({"errors": ["Missing data: price, pizza_id, or restaurant_id"]}), 400)

        if not (1 <= price <= 30):
            return make_response(jsonify({"errors": ["Price must be between 1 and 30"]}), 400)

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza:
            return make_response(jsonify({"errors": ["Pizza not found"]}), 404)
        if not restaurant:
            return make_response(jsonify({"errors": ["Restaurant not found"]}), 404)

        try:
            new_restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
            )
            db.session.add(new_restaurant_pizza)
            db.session.commit()
            return make_response(jsonify(new_restaurant_pizza.to_dict()), 201)

        except IntegrityError:
            db.session.rollback()
            return make_response(jsonify({"errors": ["Failed to create RestaurantPizza due to data integrity issue."]}), 400)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 500)
        
api.add_resource(RestaurantPizzaCreate, '/restaurant_pizzas')