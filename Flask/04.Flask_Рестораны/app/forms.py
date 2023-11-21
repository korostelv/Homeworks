from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RestaurantForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    specialization = StringField('Специализация', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    website = StringField('Сайт', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[DataRequired()])

    submit = SubmitField("Отправить")
