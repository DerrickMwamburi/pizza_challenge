from server.config import db
from sqlalchemy.orm import relationship


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade="all, delete-orphan",
        lazy=True
    )

    def to_dict(self):
        
        pizzas_data = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": pizzas_data
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

    def __repr__(self):
        return f'<Restaurant {self.name}>'