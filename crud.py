from model import db, User, Favorites, Recipes, Ingredient, connect_to_db

def create_user(user_name, password):

    user = User(user_name = user_name, password = password)

    return user

def get_user_by_username(user_name):
    
    return User.query.filter(User.user_name == user_name).first()