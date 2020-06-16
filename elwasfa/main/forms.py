from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm



class ContactForm(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    subject = StringField('Subject', validators = [DataRequired()])
    messages = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
