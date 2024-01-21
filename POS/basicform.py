from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AddItems(FlaskForm):
    barcode = StringField('barcode', validators=[DataRequired()])
    brand_name = StringField('brand_name',
                        validators=[DataRequired()])
    product_name = StringField('product_name',
                        validators=[DataRequired()])
    size = IntegerField('size',
                       validators=[DataRequired()])

    available_units = StringField('unit',
                       validators=[DataRequired()])

    MRP = IntegerField('MRP',
                        validators=[DataRequired()])

    buying_price = IntegerField('buying_price',
                        validators=[DataRequired()])
    selling_price = StringField('selling_price')

    buying_from = StringField('buying_from')
    submit = SubmitField("Submit")

    # def __init__(self, brand, product_name, size, unit):
    #     self.brand = brand
    #     self.product_name = product_name
    #     self.size = size
    #     self.unit = unit
