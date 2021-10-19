from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField,RadioField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrarUsuario(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=20)])
    apellido = StringField("Apellido", validators=[DataRequired(), Length(min=2, max=20)])
    email  = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=30)])
    cellphone = StringField("Celular", validators=[DataRequired(), Length(min=7, max=20)])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    password =  PasswordField("Contraseña", validators=[
        DataRequired(),
        Length(min=6, max=10),
        EqualTo('password_confirm')
    ])
    password_confirm = PasswordField("Confimarción de contraseña", validators=[DataRequired(), Length(min=6, max=10)])
    Rol= RadioField('Rol', choices=[('is_Admin','Administrador'),('is_Docente','Docente'), ('is_Estudiante','Etudiante')])


    submit = SubmitField("Registrar")
  

