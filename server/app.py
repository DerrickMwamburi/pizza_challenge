from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('server.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import controllers to register routes
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller