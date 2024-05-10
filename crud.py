from model import db, User, Favorites, Recipes, Ingredient, RecipeRating, connect_to_db

def create_user(user_name, password):

    user = User(user_name = user_name, password = password)

    return user

def get_user_by_username(user_name):
    
    return User.query.filter(User.user_name == user_name).first()

def get_recipes():

    return Recipes.query.all()

def get_recipe_by_id(recipe_id):

    recipe = Recipes.query.get(recipe_id)
    recipe.rating = RecipeRating.query.filter_by(recipe_id = recipe_id).first()

    return recipe

def create_recipe(description, recipe_name, instructions, ingredients_data):

    recipe = Recipes(description = description, name = recipe_name, instructions = instructions )

    db.session.add(recipe)
    db.session.commit()

    for ingredient_data in ingredients_data:
        ingredient_name, measurement, unit = ingredient_data
        ingredient = Ingredient(ingredient_name=ingredient_name, measurement=measurement, unit=unit, recipe_id=recipe.id)
        db.session.add(ingredient)

    db.session.commit()

    return recipe

def create_rating(user, recipe, rating):

    rating = RecipeRating(user = user, recipe = recipe, rating = rating)

    return rating

def add_update_rating(recipe_id, user_id, rating, comment):

    existing_rating = RecipeRating.query.filter_by(recipe_id=recipe_id, user_id=user_id).first()

    if existing_rating:
        existing_rating.rating = rating
        existing_rating.comment = comment
    else:
        new_rating = RecipeRating(recipe_id=recipe_id, user_id=user_id, rating=int(rating), comment=comment)
        db.session.add(new_rating)

    db.session.commit()

def is_favorite(user_id, recipe_id):

    favorite = Favorites.query.filter_by(user_id = user_id, recipe_id = recipe_id).first()
    return favorite is not None

def add_favorite(user_id, recipe_id):

    favorite = Favorites(user_id = user_id, recipe_id = recipe_id)
    if not favorite:
        favorite = Favorites(user_id = user_id, recipe_id = recipe_id)
        db.session.add(favorite)
        db.session.commit()

def remove_favorite(user_id, recipe_id):

    favorite = Favorites.query.filter_by(user_id = user_id, recipe_id = recipe_id).first()
    if not favorite:
        db.session.delete(favorite)
        db.session.commit()




    # rating.rating = new_rating ### need to clarify if this will work ###