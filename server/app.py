from server.config import app, db, migrate, api 
from server.models.restaurant import Restaurant 
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp


app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def home():
    return "<h1>Welcome to the Pizza Restaurant API!</h1>"


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Restaurant=Restaurant, Pizza=Pizza, RestaurantPizza=RestaurantPizza)