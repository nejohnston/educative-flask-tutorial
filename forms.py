"""
WTForms
Nicholas Johnston
December 31, 2020
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    full_name = StringField('Full Name')
    email = StringField('Email')
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm', validators=[EqualTo('password'), InputRequired()])
    submit = SubmitField('Sign Up')
