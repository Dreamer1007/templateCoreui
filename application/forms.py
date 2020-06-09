from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from application import db, app
from application.models import User, Role

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('that username is taken. please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('that email is taken. please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    def Role():
        """
    Populate a small db with some example entries.
    """

        import string
        import random

        db.drop_all()
        db.create_all()

        with app.app_context():
            user_role = Role(name='user')
            super_user_role = Role(name='superuser')
            db.session.add(user_role)
            db.session.add(super_user_role)
            db.session.commit()

            test_user = user_datastore.create_user(
                username='Admin',
                email='admin',
                password=encrypt_password('admin'),
                roles=[user_role, super_user_role]
            )
            
        