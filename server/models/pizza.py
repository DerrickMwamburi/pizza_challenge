from server.config import db
from sqlalchemy.orm import relationship # Import relationship for defining relationships


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    # Define relationship with RestaurantPizza
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='pizza',
        lazy=True # Load related objects only when accessed
    )

    def to_dict(self):
        """
        Serializes the Pizza object.
        """
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

    def serialize(self):
        """
        Serializes the Pizza object (same as to_dict for this model).
        """
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

    def __repr__(self):
        return f'<Pizza {self.name}>'