from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from form import UsernameForm
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'user'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@user/username'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'

db = SQLAlchemy(app)
# mysql = MySQL(app)


class Username(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)


@app.route('/')
def home_page():
    return '<h1>New Hello World!</h1>'


@app.route('/username', methods=['GET', 'POST'])
def add_username():
    if request.method == 'POST':
        # user = request.form['username']
        # cursor = mysql.connection.cursor()
        # print(user)
        # cursor.execute('''INSERT INTO username (name) VALUES(%s)''', [user])
        # mysql.connection.commit()
        # cursor.close()
        # return render_template('add_username.html', form=form)

        """Add entries to DB for sqllite"""
        username = request.form.get("username")
        entries = Username(username=username)
        db.session.add(entries)
        db.session.commit()
        print(entries.username)
        return redirect(url_for('show_all_username'))

    form = UsernameForm()
    return render_template('add_username.html', form=form)


@app.route('/create_tables')
def create_table():
    db.create_all()
    return "<h1> Table was created successfully</h1>"


@app.route('/show_all')
def show_all_username():
    # pass
    all_records = Username.query.all()
    return render_template('show_data.html', users=all_records)


if __name__ == '__main__':
    app.run(debug=True)
