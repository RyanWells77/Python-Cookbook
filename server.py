
from flask import Flask, render_template, request, flash, session, redirect
from flask_bcrypt import Bcrypt
from forms import LoginForm 
from model import User, Favorites, Recipes, Ingredient, db, connect_to_db



import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
bcrypt = Bcrypt(app)


@app.route("/")
def homepage():

    return render_template("home.html")

@app.route("/create_user", methods = ["POST"])
def new_user():

    user_name = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(user_name)
    if user:
        flash(f"A user with the name {user_name} allready exists. Please choose a different name.")
    else:
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = crud.create_user(user_name, hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account {user_name} created! Please login with {user_name}.")

    return redirect("/")


# @app.route("/login", methods = ["GET", "POST"])
# def login():
#     user_name = login_form.username.data
#     password = login_form.password.data

#     user = User.query.filter_by(user_name = user_name).first()

if __name__ == "__main__":
    connect_to_db(app)

    # create_database()

    db.create_all()

    app.run(debug=True)


