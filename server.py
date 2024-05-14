
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify 
from flask_bcrypt import Bcrypt
from forms import LoginForm, NewUserForm, NewRecipe 
from model import User, Favorites, Recipes, Ingredient, db, connect_to_db, RecipeRating



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

    user_id = session.get("user_id")
    print(f"user id is: ", user_id)
    return render_template("home.html", user_id = user_id)

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

    #### print statments for debugging ####
    # for recipe in recipes:
    #     print(vars(recipe))
    # print(vars(recipes[0]))

    return render_template("recipes_list.html", recipes = recipes)

@app.route("/recipe/<recipe_id>")
def recipe_details(recipe_id):

    user_id = session.get("user_id")

    #### Use to get the name attached to the id ####
    # if user_id:
    #     user = User.query.get(user_id)
    #     if user:
    #         user_name = user.user_name
    #         print(user_name)

    recipe = crud.get_recipe_by_id(recipe_id, user_id)

    is_favorite = False
    if user_id:
        is_favorite = crud.is_favorite(user_id, recipe_id)

    ingredients = recipe.ingredients
    rating = None
    if user_id:
        rating = RecipeRating.query.filter_by(recipe_id = recipe_id, user_id = user_id).first()

    #### print statments for debugging ####
    # print("this is the type: ",type(rating))
    # print("this is the value for rating: ",rating)

    return render_template("recipe_details.html", recipe = recipe, ingredients = ingredients, rating = rating, is_favorite = is_favorite)

@app.route("/add_rating/<recipe_id>", methods = ["POST", "GET"])
def add_rating(recipe_id):
    if request.method == "POST":
        user_id = session.get("user_id")
        rating = int(request.form["rating"])
        comment = request.form["comment"]

        crud.add_update_rating(recipe_id, user_id, rating, comment)
        flash("Rating and Comment added.")
        return redirect(url_for("recipe_details", recipe_id=recipe_id))
    elif request.method == "GET":
        pass

@app.route("/add_recipe", methods=["GET","POST"])
def add_recipe():
    if request.method == "POST":
        # Extract recipe data from the JSON
        data = request.get_json()

        #### print statment for debugging ####
        # print("this is the data in the request: ", data)

        recipe_name = data.get('name')
        description = data.get('description')
        instructions = data.get('instructions')

        # Extract ingredients data from the JSON
        ingredients_data = data.get('ingredients')

        # Validate the presence of required fields
        if not (description and recipe_name and instructions and ingredients_data):
            return jsonify({'error': 'Incomplete data. Required fields are missing.'}), 400

        # Insert the recipe and ingredients into the database
        try:
            recipe = crud.create_recipe(description, recipe_name, instructions, ingredients_data)
            return jsonify({'message': 'Recipe added successfully', 'recipe_id': recipe.id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return redirect("/home")


@app.route("/add_update_favorite/<recipe_id>")
def add_update_favorite(recipe_id):

    user_id = session.get("user_id")

    if user_id:
        is_favorite = crud.is_favorite(user_id, recipe_id)

        if is_favorite:
            crud.remove_favorite(user_id, recipe_id)
            is_favorite = False  # Recipe is no longer a favorite
        else:
            crud.add_favorite(user_id, recipe_id)
            is_favorite = True  # Recipe is now a favorite
        return jsonify({"is_favorite": is_favorite})
    
@app.route("/favorites/<user_id>", methods = ["GET"])
def get_favorites_list(user_id):
    
    favorites = crud.get_favorites(user_id)

    #### trying to print recipe name of favorite recipes for debugging ####
    # print("This is suposed to be the recipe name", favorites[0].recipe.name)

    return render_template("favorites_list.html", favorites = favorites )



if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    app.run(debug=True)


