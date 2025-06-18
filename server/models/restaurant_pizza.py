from server.config import db
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    restaurant = relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = relationship('Pizza', back_populates='restaurant_pizzas')

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
            "restaurant": self.restaurant.serialize() if self.restaurant else None,
            "pizza": self.pizza.serialize() if self.pizza else None
        }

    def serialize(self):
        return self.to_dict()

    def __repr__(self):
        return f'<RestaurantPizza id={self.id}, price={self.price}>'