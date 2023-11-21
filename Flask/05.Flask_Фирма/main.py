
from flask import render_template, flash, redirect, url_for
from app import app,db
from app.forms import CustomerForm, SellerForm, ProductForm, SaleForm
from app.models import Customer, Seller, Product, Sale


customers = Customer.query.all()
print(customers)