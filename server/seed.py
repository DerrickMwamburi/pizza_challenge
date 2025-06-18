from server.app import app, db # Import app and db from app.py
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_database():
    with app.app_context(): # Ensure we are in the Flask application context
        print("Clearing existing data...")
        # Clear existing data in reverse order of dependency
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        db.session.commit()
        print("Data cleared.")

        print("Seeding Restaurants...")
        r1 = Restaurant(name='Derrick Pizzaria', address='Athi-River')
        r2 = Restaurant(name='Pizza innit', address='South B')
        r3 = Restaurant(name='Sanaipei Pizzaria', address='Utawala')
        db.session.add_all([r1, r2, r3])
        db.session.commit()
        print("Restaurants seeded.")

        print("Seeding Pizzas...")
        p1 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
        p2 = Pizza(name='Veggie Delight', ingredients='Dough, Tomato Sauce, Cheese, Mushrooms, Olives')
        p3 = Pizza(name='Margherita', ingredients='Dough, Tomato Sauce, Mozzarella, Basil')
        p4 = Pizza(name='Hawaiian', ingredients='Dough, Tomato Sauce, Cheese, Ham, Pineapple')
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        print("Pizzas seeded.")

        print("Seeding RestaurantPizzas...")
        rp1 = RestaurantPizza(restaurant=r1, pizza=p1, price=1200)
        rp2 = RestaurantPizza(restaurant=r1, pizza=p2, price=1400)

        rp3 = RestaurantPizza(restaurant=r2, pizza=p3, price=1000)
        rp4 = RestaurantPizza(restaurant=r2, pizza=p4, price=1500)

        rp5 = RestaurantPizza(restaurant=r3, pizza=p1, price=1300)
        rp6 = RestaurantPizza(restaurant=r3, pizza=p3, price=1100)

        db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6])
        db.session.commit()
        print("RestaurantPizzas seeded.")
        print("Database seeding complete!")

if __name__ == '__main__':
    seed_database()