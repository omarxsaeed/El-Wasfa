from elwasfa import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    displayname = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='commenter', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.displayname}', '{self.email}', '{self.image_file}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(120), nullable=False)
    prep = db.Column(db.Integer, nullable=False)
    cook = db.Column(db.Integer, nullable=False)
    ready = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ingredients = db.relationship('Ingredient', backref='recipe_ingredient', lazy=True)
    directions = db.relationship('Direction', backref='recipe_direction', lazy=True)
    comments = db.relationship('Comment', backref='recipe_comment', lazy=True)

    def __repr__(self):
        return f"Recipe('{self.id}','{self.name}', '{self.description}','{self.user_id}', '{self.picture}')"

    def as_dict(self):
        return {'name': self.name}

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.comment}', '{self.date_posted}', '{self.user_id}', '{self.recipe_id}')"

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredient = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __repr__(self):
        return f"Ingredient('{self.id}', '{self.ingredient}', '{self.user_id}', '{self.recipe_id}')"

class Direction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    direction = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __repr__(self):
        return f"Direction('{self.id}', '{self.direction}', '{self.user_id}', '{self.recipe_id}')"

