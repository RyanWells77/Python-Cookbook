import os
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)


    def get_all_favorites(self):
        favorites = []

        for favorite in self.user_favorites:
            favorites.append(favorite.recipe)

        return favorites
    
class Favorites(db.Model):

    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey ("users.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey ("recipes.id"), nullable = False)


class Recipes(db.Model):
    
    __tablename__ = "recipes"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    description = db.Column(db.Text)
    name = db.Column(db.String, unique = True, nullable = False)
    instructions = db.Column(db.Text, nullable = False)

    #### adding a backref to Favorites model. I hope this dosn't break anything ####

    favorites = db.relationship("Favorites", backref="recipe", lazy=True)


class Ingredient(db.Model):
    
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    ingredient_name = db.Column(db.String, nullable = False)
    measurement = db.Column(db.String, nullable = False)
    unit = db.Column(db.String, nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable = False)

    recipe_ingredients = db.relationship("Recipes", backref = "ingredients", lazy = True)

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

class RecipeRating(db.Model):
     
    __tablename__ = "recipe_ratings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)

    recipe_rating = db.relationship("Recipes", backref = "recipe_rating", lazy = True)



if __name__ == "__main__":
    from server import app
    

    connect_to_db(app)