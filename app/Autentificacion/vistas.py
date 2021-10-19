from flask import render_template as render, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from . import Autentificacion
from app.modelo import UserModel
from .formularios import LoginForm, RegistrarUsuario
from flask import Request


@Autentificacion.route('/login', methods=['GET', 'POST'])
def login():
    """ Método vista para el login de usuarios. """
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }


    if login_form.validate_on_submit():
        pass


    return render('Autentificacion/Login.html', **context)

@Autentificacion.route('/Login2',methods=['GET', 'POST'])
def login2():
  return render('Autentificacion/Login2.html')