from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from basicform import RegistrationForm, LoginForm, AddItems
from flask_mysqldb import MySQL
import datetime

# db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'POS'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://madhur:@localhost/POS'
# db.init_app(app)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'POS'
mysql = MySQL(app)


# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#
#     # def __repr__(self):
#     #     return f"User({self.username}, {self.email}, {self.password})"
#
#
# class Add_items(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # added_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     # barcode = db.Column(db.String(120))
#     brand = db.Column(db.String(120), nullable=False)
#     product_name = db.Column(db.String(120), nullable=False)
#     size = db.Column(db.Integer, nullable=False)
#     unit = db.Column(db.Integer, nullable=False)
#
#     # mrp = db.Column(db.Integer)
#
#     def __repr__(self):
#         return '<name %r>' % self.name
#
#     # cur = mysql.connection.cursor()
#     # cur.execute("INSERT INTO POS(id,brand,name,size,unit,mrp) VALUES (%s %s %s %s %s %s)",())
#
#
# my_dict = {'name': 'Madhur'}
# my_list = ['Madhur', 30]
# my_str = 'Madhur'


@app.route('/')
def grt_hello():
    return '<h1> Hello World!</h1>'


# @app.route('/dict')
# def print_dict():
#     return render_template('basic.html', my_dict=my_dict)
#
#
# @app.route('/list')
# def print_list():
#     return render_template('basic.html', my_list=my_list)
#
#
# @app.route('/str')
# def print_str():
#     return render_template('basic.html', my_str=my_str)
#
#
# @app.route('/<username>')
# def print_user(username):
#     return render_template('basic.html', my_variable=username)  # '<p> I am on page for {}'.format(username)

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/bill')
def make_bill():
    return render_template('billing.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        # Need to add tables in phpmyadmin
        cursor.execute('''INSERT INTO customer (username, email, password)
                VALUES(%s, %s, %s)''',
                       [username, email, password])
        mysql.connection.commit()
        cursor.close()
    return render_template('register.html', form=form)


# @app.route('/create_tables')
# def create_table():
#     db.create_all()
#     return "<h1> Table was created successfully</h1>"


# @app.route('/show_all')
# def show_all():
#     all_records = Add_items.query.all()
#     return render_template('show_data.html', data=all_records)


@app.route('/additems', methods=['GET', 'POST'])
def add_items():
    form = AddItems()
    if request.method == 'POST':
        pass

        # return render_template('add_item.html', form=form)

    if form.validate_on_submit():
        barcode = request.form['barcode']
        brand_name = request.form['brand_name']
        product_name = request.form['product_name']
        size = request.form['size']
        available_units = request.form['available_units']
        MRP = request.form['MRP']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        buying_from = request.form['buying_from']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO items (barcode, brand_name, product_name, size, available_units, MRP, buying_price, 
                selling_price, purchase_from) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       [barcode, brand_name, product_name, size, available_units, MRP, buying_price, selling_price,
                        buying_from])
        mysql.connection.commit()
        cursor.close()
        # do stuff with valid form
        # then redirect to "end" the form
        return redirect(url_for('add_items'))

        # """Add entries to DB"""
        # brand = request.form.get("brand")
        # product_name = request.form.get("product_name")
        # size = request.form.get("size")
        # unit = request.form.get("unit")
        # entries = Add_items(brand=brand, product_name=product_name, unit=unit, size=size)
        # db.session.add(entries)
        # db.session.commit()
        # return redirect(url_for('show_all'))
    return render_template('add_item.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
