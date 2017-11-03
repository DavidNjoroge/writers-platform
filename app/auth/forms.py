from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email=StringField('your email address',validators=[Required(),Email()])
    username=StringField('Enter your username',validators=[Required()])
    password=PasswordField('password',validators=[Required(),
    EqualTo('password',message='password must match')])
    password_confirm=PasswordField('confirm passwords',validators=[Required()])
    submit=SubmitField('signup')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('there is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('there is a username with that name')
class LoginForm(FlaskForm):
    email=StringField('your email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Sign in')
