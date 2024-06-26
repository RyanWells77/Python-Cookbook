from model import db, User, Favorites, Recipes, Ingredient, RecipeRating, connect_to_db

def create_user(user_name, password):

    user = User(user_name = user_name, password = password)

    return user

def get_user_by_username(user_name):
    
    return User.query.filter(User.user_name == user_name).first()

def get_recipes():

    return Recipes.query.all()

def get_recipe_by_id(recipe_id, user_id):

    
    recipe = Recipes.query.get(recipe_id)
    recipe.rating = RecipeRating.query.filter_by(recipe_id = recipe_id).first()
    recipe.favorite = Favorites.query.filter_by(user_id = user_id, recipe_id = recipe_id).first()
    #### print for debugging ####
    # print(recipe.favorite)

    return recipe

def create_recipe(description, recipe_name, instructions, ingredients_data):

    recipe = Recipes(description = description, name = recipe_name, instructions = instructions )

    db.session.add(recipe)
    db.session.commit()

    recipe_id = recipe.id

    for ingredient_data in ingredients_data:
        ingredient_name = ingredient_data.get('ingredient_name')
        measurement = ingredient_data.get('measurement')
        unit = ingredient_data.get('unit')

            # Create and add the Ingredient to the session
        ingredient = Ingredient(ingredient_name=ingredient_name, measurement=measurement, unit=unit, recipe_id=recipe_id)
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

def get_favorites(user_id):

    favorites_list = Favorites.query.filter_by(user_id = user_id).all()

    return favorites_list

def is_favorite(user_id, recipe_id):

    favorite = Favorites.query.filter_by(user_id = user_id, recipe_id = recipe_id).first()
    #### print for debugging ####
    # print("favorite" ,favorite)
    return favorite is not None

def add_favorite(user_id, recipe_id):

    favorite = Favorites(user_id = user_id, recipe_id = recipe_id)

    db.session.add(favorite)
    db.session.commit()

def remove_favorite(user_id, recipe_id):

    favorite = Favorites.query.filter_by(user_id = user_id, recipe_id = recipe_id).first()

    db.session.delete(favorite)
    db.session.commit()




    # rating.rating = new_rating ### need to clarify if this will work ###