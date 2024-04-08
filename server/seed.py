from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()
    

   
    restaurants = []
    restaurants.append(Restaurant(name='Karen Blixen', address='123 Karen Rd'))
    restaurants.append(Restaurant(name='Artcaffe', address='456 Raphta St'))
    restaurants.append(Restaurant(name='Burger Haven', address='789 Burger Blvd')),
    restaurants.append(Restaurant(name='Sushi Station', address='101 Sushi Lane')),
    restaurants.append(Restaurant(name='Taco Fiesta', address='234 Taco Rd')),
    restaurants.append(Restaurant(name='BBQ Barn', address='567 BBQ Blvd')), 
    restaurants.append(Restaurant(name='Curry Kingdom', address='890 Curry St')),
    restaurants.append(Restaurant(name='Noodle House', address='111 Noodle Ave')),
    restaurants.append(Restaurant(name='Salad Oasis', address='222 Salad Blvd')),
    restaurants.append(Restaurant(name='Dessert Dream', address='333 Dessert St'))
    db.session.add_all(restaurants)

   
    pizzas = []
    pizzas.append(
        Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil'))
    pizzas.append(
        Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni'))
    pizzas.append(
        Pizza(name='Vegetarian', ingredients='Tomato, Mozzarella, Mixed Vegetables'))
    pizzas.append(
        Pizza(name='Hawaiian', ingredients='Tomato, Mozzarella, Ham, Pineapple'))
    pizzas.append(
        Pizza(name='BBQ Chicken', ingredients='BBQ Sauce, Mozzarella, Chicken, Red Onion'))
    pizzas.append(
        Pizza(name='Supreme', ingredients='Tomato, Mozzarella, Pepperoni, Mushroom, Bell Pepper, Olive'))
    pizzas.append(
        Pizza(name='Seafood', ingredients='Tomato, Mozzarella, Shrimp, Calamari, Clam'))
    pizzas.append(
        Pizza(name='Mushroom Lovers', ingredients='Tomato, Mozzarella, Mushroom Variety'))
    pizzas.append(
        Pizza(name='Meat Feast', ingredients='Tomato, Mozzarella, Sausage, Bacon, Ham, Pepperoni'))
    pizzas.append(
        Pizza(name='Four Cheese', ingredients='Mozzarella, Cheddar, Gorgonzola, Parmesan'))

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
    restaurant_pizzas.append(RestaurantPizza(price=11,
                             restaurant=restaurants[2], pizza=pizzas[2]))
    restaurant_pizzas.append(RestaurantPizza(price=13,
                             restaurant=restaurants[3], pizza=pizzas[3]))
    restaurant_pizzas.append(RestaurantPizza(price=15,
                             restaurant=restaurants[4], pizza=pizzas[4]))
    restaurant_pizzas.append(RestaurantPizza(price=14,
                             restaurant=restaurants[5], pizza=pizzas[5]))
    restaurant_pizzas.append(RestaurantPizza(price=16,
                             restaurant=restaurants[6], pizza=pizzas[6]))
    restaurant_pizzas.append(RestaurantPizza(price=17,
                             restaurant=restaurants[7], pizza=pizzas[7]))
    restaurant_pizzas.append(RestaurantPizza(price=18,
                             restaurant=restaurants[8], pizza=pizzas[8]))
    restaurant_pizzas.append(RestaurantPizza(price=19,
                             restaurant=restaurants[9], pizza=pizzas[9]))
    db.session.add_all(restaurant_pizzas)

    db.session.commit()
