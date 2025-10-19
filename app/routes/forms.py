from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class Registration(FlaskForm):
    name = StringField('Username',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    register = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    login= SubmitField('Login')
    
