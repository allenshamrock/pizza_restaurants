from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules=('-restaurantpizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    #relationship to RestaurantPizza
    restaurantpizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    @validates('name')
    def validate_name(self,key,name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name={self.name}, address={self.address})>"


class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurantpizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    #relationship to RestaurantPizza
    restaurantpizzas = db.relationship('RestaurantPizza', back_populates='pizza')


class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurantpizzas'
    serialize_rules = ('-restaurant.restaurantpizzas','-pizza.restaurantpizzas')


    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    # relationship to Restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurantpizzas')

    # relationship to Pizza
    pizza = db.relationship('Pizza', back_populates='restaurantpizzas')

    @validates('price')
    def validate_price(self,key,price):
        if not 1 <= price <= 30:
            raise ValueError('Price must be between 1 and 30')
        return price
