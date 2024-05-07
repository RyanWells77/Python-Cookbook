from model import db, User, Favorites, Recipes, Ingredient, RecipeRating, connect_to_db

def create_user(user_name, password):

    user = User(user_name = user_name, password = password)

    return user

def get_user_by_username(user_name):
    
    return User.query.filter(User.user_name == user_name).first()

def get_recipes():

    return Recipes.query.all()

def get_recipe_by_id(recipe_id):

    return Recipes.query.get(recipe_id)

def create_rating(user, recipe, rating):

    rating = RecipeRating(user = user, recipe = recipe, rating = rating)

    return rating

def update_rating(rating_id, new_rating):

    rating = RecipeRating.query.get(rating_id)

def create_recipe(description, recipe_name, instructions, ingredients_data):

    recipe = Recipes(description = description, recipe_name = recipe_name, instructions = instructions )

    db.session.add(recipe)
    db.session.commit()

    for ingredient_data in ingredients_data:
        ingredient_name, measurement, unit = ingredient_data
        ingredient = Ingredient(ingredient_name=ingredient_name, measurement=measurement, unit=unit, recipe_id=recipe.id)

        db.session.add(ingredient)
    db.session.commit()

    return recipe

    # rating.rating = new_rating ### need to clarify if this will work ###