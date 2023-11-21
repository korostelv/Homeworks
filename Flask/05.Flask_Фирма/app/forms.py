from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, EmailField, TextAreaField, TelField, FloatField
from wtforms.validators import DataRequired, Email


class CustomerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    phone = TelField('Номер телефона', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField("Отправить")


class SellerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    date_employ = DateField('Дата приема на работу', validators=[DataRequired()])
    position = SelectField('Позиция в фирме:', choices=['Продавец', 'Старший продавец','Руководитель отдела продаж'],validators=[DataRequired()])
    submit = SubmitField("Отправить")


class ProductForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    specification = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField("Отправить")


class SaleForm(FlaskForm):
    customer = SelectField('Клиент', coerce=int, validators=[DataRequired()])
    seller = SelectField('Продавец', coerce=int, validators=[DataRequired()])
    product = SelectField('Продукт', coerce=int, validators=[DataRequired()])
    date_sale = DateField('Дата продажи', validators=[DataRequired()])
    summ = FloatField('Сумма продажи', validators=[DataRequired()])
    submit = SubmitField('Создать продажу')


# class SaleForm(FlaskForm):
#     customer = SelectField('Клиент', validators=[DataRequired()])
#     seller = SelectField('Продавец', validators=[DataRequired()])
#     product = SelectField('Продукт', validators=[DataRequired()])
#     date_sale = DateField('Дата продажи', validators=[DataRequired()])
#     summ = FloatField('Сумма продажи', validators=[DataRequired()])
#     submit = SubmitField('Создать продажу')



