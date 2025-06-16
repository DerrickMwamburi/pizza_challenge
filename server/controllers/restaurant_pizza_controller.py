from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate input
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({'errors': ['Missing required fields']}), 400

    # Validate price range
    try:
        price = int(price)
        if price < 1 or price > 30:
            return jsonify({'errors': ['Price must be between 1 and 30']}), 400
    except ValueError:
        return jsonify({'errors': ['Price must be an integer']}), 400

    # Check if restaurant and pizza exist
    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)
    if not restaurant or not pizza:
        return jsonify({'errors': ['Restaurant or Pizza not found']}), 404

    # Create new RestaurantPizza
    restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify(restaurant_pizza.to_dict()), 201