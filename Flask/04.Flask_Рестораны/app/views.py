from flask import render_template, flash, redirect, url_for
from app import app,db
from app.forms import RestaurantForm
from app.models import Restaurant
from sqlalchemy.exc import IntegrityError

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = RestaurantForm()
    if form.validate_on_submit():
        try:
            rest = Restaurant(
                name=form.name.data,
                specialization=form.specialization.data,
                address=form.address.data,
                website=form.website.data,
                phone=form.phone.data
            )
            db.session.add(rest)
            db.session.commit()
            flash('Добавлен ресторан {}'.format(form.name.data))
            # return render_template('index.html', form=form)
        except IntegrityError as e:
            db.session.rollback()
            flash('Ресторан с именем {} уже существует'.format(form.name.data))
            return render_template('form.html', form=form)
    return render_template('form.html', form=form)


@app.route('/display')
def display():
    restaurants = Restaurant.query.all()
    spec = set()
    for rest in restaurants:
        spec.add(rest.specialization)
    return render_template('display.html', restaurants=restaurants, spec=spec)


@app.route('/<int:id>/delete')
def delete(id):
    rest = Restaurant.query.get(id)
    db.session.delete(rest)
    db.session.commit()
    return redirect(url_for('display'))


@app.route('/<int:id>/change', methods=['GET', 'POST'])
def change(id):
    rest = Restaurant.query.get(id)
    if rest is None:
        return "Ресторан не найден", 404
    form = RestaurantForm(obj=rest)
    if form.validate_on_submit():
        rest.name = form.name.data
        rest.specialization = form.specialization.data
        rest.address = form.address.data
        rest.website = form.website.data
        rest.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('display'))
    return render_template('change.html', form=form, rest=rest)


@app.route('/<specialization>/spec')
def spec(specialization):
    restaurants = Restaurant.query.filter_by(specialization=specialization).all()
    return render_template('spec.html', restaurants=restaurants,specialization=specialization)