from server.config import db
from sqlalchemy import CheckConstraint # Import CheckConstraint for validation
from sqlalchemy.orm import relationship # Import relationship for defining relationships


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Define relationships with Restaurant and Pizza
    restaurant = relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = relationship('Pizza', back_populates='restaurant_pizzas')

    # Add CheckConstraint for price validation
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price'),
    )

    def to_dict(self):
        """
        Serializes the RestaurantPizza object, including nested Restaurant and Pizza details.
        """
        return {
            "id": self.id,
            "price": self.price,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
            "restaurant": self.restaurant.serialize() if self.restaurant else None, # Include serialized restaurant
            "pizza": self.pizza.serialize() if self.pizza else None # Include serialized pizza
        }

    def serialize(self):
        """
        Serializes the RestaurantPizza object (same as to_dict for this model).
        """
        return self.to_dict()

    def __repr__(self):
        return f'<RestaurantPizza id={self.id}, price={self.price}>'