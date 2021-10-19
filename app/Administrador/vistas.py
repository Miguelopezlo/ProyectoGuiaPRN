from flask import render_template as render, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from . import Administrador
from app.modelo import UserModel
from .formularios import  RegistrarUsuario


@Administrador.route('/registrar', methods=['GET', 'POST'])
def signup():
    """ Método vista para el registro de usuarios. """
    register_form = RegistrarUsuario()
    context = {
        'register_form': register_form
    }



    if register_form.validate_on_submit():
        pass


    return render('Administrador/CrearUsuario.html', **context)

