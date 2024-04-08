from flask import Flask,request,make_response,jsonify
from flask_migrate import Migrate
from models import db,Restaurant,RestaurantPizza,Pizza
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False

migrate = Migrate(app,db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Pizza Restaurants API</h1>'


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    if request.method == 'GET':
        restaurants = [
            {
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address
        } for restaurant in Restaurant.query.all()]
        response = make_response(
            jsonify(restaurants),
            200
        )

        return response


@app.route('/restaurants/<int:id>')
def restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": []
        }
        for pizza in restaurant.pizzas:
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            restaurant_data["pizzas"].append(pizza_data)

        response = make_response(jsonify(restaurant_data), 200)
        return response
    else:
        response_body = {
            "Error": "Restaurant not found."
        }
        response = make_response(jsonify(response_body), 404)
        return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)
