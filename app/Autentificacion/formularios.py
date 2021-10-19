from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    """ Formulario de login. """
    username = StringField("Usuario", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, max=10)])

    submit = SubmitField("Login")