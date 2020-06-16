from elwasfa.models import Recipe
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class AddRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(), Length(min = 4 , max = 40)])
    description = StringField('Description', validators=[DataRequired(), Length(min = 10 , max = 500)])
    picture = FileField('Add Recipe Picture', validators=[DataRequired(), FileAllowed(["jpeg", "jpg", "png"])])
    ingredient_1 = StringField('Ingredients', validators=[DataRequired(), Length(min = 2 , max = 40)])
    prep_time = IntegerField('Prep Time', validators=[DataRequired()])
    cook_time = IntegerField('Cooking Time', validators=[DataRequired()])
    ready_time = IntegerField('Ready In', validators=[DataRequired()])
    direction_1 = StringField('Directions', validators=[DataRequired(), Length(min = 2 , max = 300)])
    submit = SubmitField('Add Recipe')

    def validate_recipename(self, recipe_name):
        recipe = Recipe.query.filter_by(name=recipe_name.data).first()
        if recipe:
            raise ValidationError('That recipe name is taken. Please choose a different one.')

class UpdateRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(), Length(min = 4 , max = 40)])
    description = StringField('Description', validators=[DataRequired(), Length(min = 10 , max = 500)])
    picture = FileField('Add Recipe Picture', validators=[FileAllowed(["jpeg", "jpg", "png"])])
    ingredient_1 = StringField('Ingredients')
    prep_time = IntegerField('Prep Time', validators=[DataRequired()])
    cook_time = IntegerField('Cooking Time', validators=[DataRequired()])
    ready_time = IntegerField('Ready In', validators=[DataRequired()])
    direction_1 = StringField('Directions')
    submit = SubmitField('Add Recipe')

    def validate_recipename(self, recipe_name):
        recipe = Recipe.query.filter_by(name=recipe_name.data).first()
        if recipe:
            raise ValidationError('That recipe name is taken. Please choose a different one.')

class CommentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Reply')

