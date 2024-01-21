from flask_sqlalchemy import SQLAlchemy
from main_script import app

# db = SQLAlchemy()
# db.init_app(app)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'
db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.password})"


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    product_name = db.Column(db.String(120), nullable=False)
    unit = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Integer, nullable=False)
