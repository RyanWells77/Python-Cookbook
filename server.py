
from flask import Flask, render_template, request, flash, session, redirect
from flask_bcrypt import Bcrypt
from forms import LoginForm, NewUserForm, NewRecipe 
from model import User, Favorites, Recipes, Ingredient, db, connect_to_db



import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
bcrypt = Bcrypt(app)


@app.route("/")
def login_page():

    user_form = NewUserForm()
    login_form = LoginForm()

    return render_template("login.html", login_form = login_form, user_form = user_form)

@app.route("/home")
def homepage():

    return render_template("home.html")

@app.route("/new_user", methods = ["POST"])
def new_user():
    user_form = NewUserForm()
    login_form = LoginForm()

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

    return render_template("login.html", user_form = user_form, login_form = login_form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    user_form = NewUserForm()
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_name = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(user_name = user_name).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash(f"Login sucessful! Logged in as {user.user_name}")
            return redirect("/home")
        else:
            flash("Invalid username or password. Please try again.")

    return render_template("login.html", login_form = login_form, user_form = user_form)

@app.route("/recipes", methods = ["GET"])
def get_recipes_list():
    
    recipes = crud.get_recipes()
    # for recipe in recipes:
    #     print(vars(recipe))
    print(vars(recipes[0]))

    return render_template("recipes_list.html", recipes = recipes)

@app.route("/recipe/<recipe_id>")
def recipe_details(recipe_id):

    recipe = crud.get_recipe_by_id(recipe_id)

    ingredients = recipe.ingredients
    rating = recipe.recipe_rating
    return render_template("recipe_details.html", recipe = recipe, ingredients = ingredients, rating = rating)

@app.route("/add_rating/<recipe_id>", methods = ["POST, GET"])
def add_rating():
    pass

@app.route("/add_recipe", methods=["POST", "GET"])
def add_recipe():

    new_recipe_form = NewRecipe()

    if new_recipe_form.validate_on_submit():
        print("Form validation passed!")
        description = new_recipe_form.description.data
        recipe_name = new_recipe_form.recipe_name.data
        instructions = new_recipe_form.instructions.data
        ingredients_data = [
            (
                ingredient['ingredient_name'],
                ingredient['measurement'],
                ingredient['unit']
            )
            for ingredient in new_recipe_form.ingredients.data
        ]

        crud.create_recipe(description, recipe_name, instructions, ingredients_data)

        return redirect("/home")
    print("Form validation failed!")
    print("Errors:", new_recipe_form.errors)  # Print validation errors
    print("Data:", new_recipe_form.data)  # Print form data
    return render_template("recipe_creation.html", new_recipe_form = new_recipe_form)


if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    app.run(debug=True)


