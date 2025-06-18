from server.config import db
from sqlalchemy.orm import relationship # Import relationship for defining relationships


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    # Define relationship with RestaurantPizza
    # cascade="all, delete-orphan" ensures that when a restaurant is deleted,
    # all associated restaurant_pizzas are also deleted.
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade="all, delete-orphan",
        lazy=True # Load related objects only when accessed
    )

    def to_dict(self):
        """
        Serializes the Restaurant object, including its associated pizzas.
        Used for GET /restaurants/<int:id>
        """
        # Exclude restaurant_pizzas directly to avoid recursion,
        # instead, explicitly add serialized pizzas.
        pizzas_data = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": pizzas_data
        }

    def serialize(self):
        """
        Serializes the Restaurant object without its associated pizzas.
        Used for GET /restaurants
        """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

    def __repr__(self):
        return f'<Restaurant {self.name}>'