from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired,Email,Length

class RegistrationForm(FlaskForm):
    name = StringField("Full name",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=8,max=20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    submit = SubmitField("Register")