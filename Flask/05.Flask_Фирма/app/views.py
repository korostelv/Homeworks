from flask import render_template, flash, redirect, url_for
from app import app,db
from app.forms import CustomerForm, SellerForm, ProductForm, SaleForm
from app.models import Customer, Seller, Product, Sale



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form_customer', methods=['GET', 'POST'])
def form_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(
            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
        )
        db.session.add(customer)
        db.session.commit()
        flash('Добавлен покупатель {}'.format(f'{form.name.data} {form.surname.data}'))
        return render_template('form_customer.html', form=form)
    return render_template('form_customer.html', form=form)


@app.route('/form_seller',methods=['GET', 'POST'] )
def form_seller():
    form = SellerForm()
    if form.validate_on_submit():
        seller = Seller(
            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
            date_employ=form.date_employ.data,
            position=form.position.data
        )
        db.session.add(seller)
        db.session.commit()
        flash('Добавлен продавец {}'.format(f'{form.name.data} {form.surname.data}'))
        return render_template('form_seller.html', form=form)
    return render_template('form_seller.html', form=form)


@app.route('/form_product',methods=['GET', 'POST'] )
def form_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            specification=form.specification.data,
        )
        db.session.add(product)
        db.session.commit()
        flash('Добавлен товар {}'.format(f'{form.name.data}'))
        return render_template('form_product.html', form=form)
    return render_template('form_product.html', form=form)


@app.route('/form_sale', methods=['GET', 'POST'])
def form_sale():
    form = SaleForm()

    customers = Customer.query.all()
    sellers = Seller.query.all()
    products = Product.query.all()

    form.customer.choices = [(customer.id, f"{customer.surname} {customer.name}") for customer in customers]
    form.seller.choices = [(seller.id, f"{seller.surname} {seller.name}") for seller in sellers]
    form.product.choices = [(product.id, product.name) for product in products]

    if form.validate_on_submit():
        customer_id = form.customer.data
        seller_id = form.seller.data
        product_id = form.product.data

        sale = Sale(
            customer_id=customer_id,
            seller_id=seller_id,
            product_id=product_id,
            date_sale=form.date_sale.data,
            summ=form.summ.data
        )
        db.session.add(sale)
        db.session.commit()
        flash('Продан товар {}'.format(form.product.label.text))
        return redirect(url_for('form_sale'))
    return render_template('form_sale.html', form=form, customers=customers, sellers=sellers, products=products)


@app.route('/display')
def display():
    customers = Customer.query.all()
    sellers = Seller.query.all()
    products = Product.query.all()
    sales = Sale.query.all()
    return render_template('display.html', customers=customers,sellers=sellers,products=products,sales=sales)



