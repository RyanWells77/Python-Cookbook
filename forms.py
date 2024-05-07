from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, PasswordField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=255)])
    submit = SubmitField('Login')

class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=255)])
    submit = SubmitField('Create User')

class RatingForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired()])
    comments = TextAreaField('Comments')
    submit = SubmitField('Create Rating')

class IngredientForm(FlaskForm):
    ingredient_name = StringField("Ingredient Name", validators=[DataRequired()])
    measurement = StringField("Measurement", validators=[DataRequired()])
    unit = SelectField("Unit", choices=("lb","oz","cup","tbs","tsp","qt","pinch"))
    
class NewRecipe(FlaskForm):
    recipe_name = StringField("Recipe Name", validators=[DataRequired()])
    description = TextAreaField("Decription", validators=[Length(max=255)])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    ingredients = FieldList(FormField(IngredientForm), min_entries=1) 
   

   