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
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        response = make_response(
            restaurants,
            200
        )

        return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
