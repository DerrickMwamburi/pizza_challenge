from server.config import db
from sqlalchemy.orm import relationship


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='pizza',
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

    def __repr__(self):
        return f'<Pizza {self.name}>'