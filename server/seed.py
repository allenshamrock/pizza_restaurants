from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()
    

   
    restaurants = []
    restaurants.append(Restaurant(name='Karen Blixen', address='123 Karen Rd'))
    restaurants.append(Restaurant(name='Artcaffe', address='456 Raphta St'))
    db.session.add_all(restaurants)

   
    pizzas = []
    pizzas.append(
        Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil'))
    pizzas.append(
        Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni'))
    db.session.add_all(pizzas)

   
    # restaurant1 = Restaurant(name='Karen Blixen')
    # restaurant2 = Restaurant(name='Artcaffe')
    # pizza1 = Pizza(name='Margherita')
    # pizza2 = Pizza(name='Pepperoni')

    restaurant_pizzas = []
    restaurant_pizzas.append(RestaurantPizza(
        price=10, restaurant=restaurants[0], pizza=pizzas[0]))
    restaurant_pizzas.append(RestaurantPizza(
        price=12, restaurant=restaurants[1], pizza=pizzas[1]))
    db.session.add_all(restaurant_pizzas)

    db.session.commit()
