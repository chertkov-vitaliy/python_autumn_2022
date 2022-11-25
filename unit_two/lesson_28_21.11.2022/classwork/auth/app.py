from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import json
# password = userInput
from sea_battle import matrix


field = matrix()
# create the app
app = Flask(__name__)
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost:5432'
db.init_app(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)
    online = db.Column(db.Boolean, nullable=True)
    id_account = db.Column(db.ForeignKey('account.id'))


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    user = db.relationship('User', backref='account')


with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return render_template("index.html", title="Мое приложение!!!!")


@app.route("/account/create", methods=["GET", "POST"])
def account_create():
    if request.method == "POST":
        hashAndSalt = bcrypt.hashpw(request.form["password"].encode(), bcrypt.gensalt())
        account = Account(
            login=request.form["login"],
            password=hashAndSalt,
        )
        db.session.add(account)
        db.session.commit()
        return "OK"
        return redirect(url_for("user_detail", id=user.id))

    return render_template("account.html")



@app.route('/cancel')
def cancel():
   # connect to DB
   return  {"id": 12, "name": "Peter I"}

@app.route("/users/list")
def user_create():
    return "OK"


if __name__ == "__main__":
    app.run()

