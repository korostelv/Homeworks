from app import db
from datetime import datetime


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    surname = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.String(12), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Customer {}>'.format(self.name)

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    surname = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.String(12), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=False)
    date_employ = db.Column(db.Date)
    position = db.Column(db.Enum('Продавец', 'Старший продавец', 'Руководитель отдела продаж'), index=True, unique=False)

    def __repr__(self):
        return '<Seller {}>'.format(self.name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    specification = db.Column(db.Text(300), index=True, unique=False)

    def __repr__(self):
        return '<Product {}>'.format(self.name)


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_sale = db.Column(db.Date, default=datetime.utcnow)
    summ = db.Column(db.Float, index=True, unique=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    customer = db.relationship('Customer', backref='sales', foreign_keys=[customer_id])
    seller = db.relationship('Seller', backref='sales', foreign_keys=[seller_id])
    product = db.relationship('Product', backref='sales', foreign_keys=[product_id])

    def __repr__(self):
        return '<Sale {}>'.format(self.id)


