from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Brikl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Storefront(db.Model):
    storefront_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='storefronts')
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Microstore(db.Model):
    microstore_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='microstore')
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Catalog(db.Model):
    catalog_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    storefront_id = db.Column(db.Integer, db.ForeignKey('storefront.storefront_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.catalog_id'))
    microstore_id = db.Column(db.Integer, db.ForeignKey('microstore.microstore_id'))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    available_date = db.Column(db.DATE)
    stock_quantity = db.Column(db.Integer, nullable=False)

class ProductImage(db.Model):
    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class ProductCategory(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), primary_key=True)