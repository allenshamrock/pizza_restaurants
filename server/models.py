from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship,validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    #relationship to RestaurantPizza
    pizzas = relationship('RestaurantPizza', back_populates='restaurant')

    @validates('name')
    def validate_name(self,key,name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name={self.name}, address={self.address})>"


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    #relationship to RestaurantPizza
    restaurants = relationship('RestaurantPizza', back_populates='pizza')


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, ForeignKey('pizzas.id'))

    # relationship to Restaurant
    restaurant = relationship('Restaurant', back_populates='pizzas')

    # relationship to Pizza
    pizza = relationship('Pizza', back_populates='restaurants')

    @validates('price')
    def validate_price(self,key,price):
        if not 1 <= price <= 30:
            raise ValueError('Price must be between 1 and 30')
        return price
