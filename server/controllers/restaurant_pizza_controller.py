from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource # Import Resource from flask_restful
from server.config import db, api
from server.models.restaurant_pizza import RestaurantPizza # Import RestaurantPizza model
from server.models.restaurant import Restaurant # Import Restaurant model to check existence
from server.models.pizza import Pizza # Import Pizza model to check existence
from sqlalchemy.exc import IntegrityError # Import IntegrityError for database constraint violations

# Create a Blueprint for restaurant_pizza routes
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

class RestaurantPizzaCreate(Resource):
    def post(self):
        """
        Handles POST request for /restaurant_pizzas.
        Creates a new RestaurantPizza.
        """
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        # Input validation
        if not all([price, pizza_id, restaurant_id]):
            return make_response(jsonify({"errors": ["Missing data: price, pizza_id, or restaurant_id"]}), 400)

        # Validate price
        if not (1 <= price <= 30):
            return make_response(jsonify({"errors": ["Price must be between 1 and 30"]}), 400)

        # Check if pizza and restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza:
            return make_response(jsonify({"errors": ["Pizza not found"]}), 404)
        if not restaurant:
            return make_response(jsonify({"errors": ["Restaurant not found"]}), 404)

        # Create new RestaurantPizza instance
        try:
            new_restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
            )
            db.session.add(new_restaurant_pizza)
            db.session.commit()

            # Return serialized new_restaurant_pizza including nested pizza and restaurant details
            return make_response(jsonify(new_restaurant_pizza.to_dict()), 201) # 201 Created

        except IntegrityError:
            # This catch is primarily for other potential DB integrity errors,
            # though price validation is handled above.
            db.session.rollback()
            return make_response(jsonify({"errors": ["Failed to create RestaurantPizza due to data integrity issue."]}), 400)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 500) # Generic error for other issues

# Add the resource to the API
api.add_resource(RestaurantPizzaCreate, '/restaurant_pizzas')