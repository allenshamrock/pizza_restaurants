from flask import Flask
from flask_migrate import Migrate
from models import Restaurant,RestaurantPizza,Pizza,db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False

Migrate = (app,db)

db.init_app(app)