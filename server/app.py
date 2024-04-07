from flask import Flask
from flask_migrate import Migrate
from models import db,Restaurant,RestaurantPizza,Pizza
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False

migrate = Migrate(app,db)

db.init_app(app)