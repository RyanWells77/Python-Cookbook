
from flask import Flask, render_template, request, flash, session, redirect
from flask_bcrypt import Bcrypt
from forms import LoginForm, NewUserForm 
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

    user_form = NewUserForm()
    login_form = LoginForm()

    return render_template("home.html", login_form = login_form, user_form = user_form)

@app.route("/new_user", methods = ["POST"])
def new_user():
    user_form = NewUserForm()

    if user_form.validate_on_submit():
        user_name = user_form.username.data
        password = user_form.password.data

        existing_user = crud.get_user_by_username(user_name)
        if existing_user:
            flash(f"A user with the name {user_name} allready exists. Please choose a different name.")
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            user = crud.create_user(user_name, hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f"Account {user_name} created! Please login with {user_name}.")

    return render_template("home.html", user_form = user_form)


@app.route("/login", methods = ["GET", "POST"])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_name = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(user_name = user_name).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash(f"Login sucessful! Logged in as {user}")
        else:
            flash("Invalid username or password. Please try again.")

    return render_template("home.html", login_form = login_form)



if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    app.run(debug=True)

