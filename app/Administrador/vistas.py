from flask import render_template as render, flash, redirect, url_for
from flask_login import  login_user, logout_user, login_required
from flask_login.utils import login_user
from . import Administrador
from app.modelo import UserModel
from .formularios import  RegistrarUsuario
from app.servicios import get_user_by_username, registro_usuarios



@login_required
@Administrador.route('/Inicio', methods = ['GET', 'POST'])
def Inicio():
    return render('Administrador/Inicio.html')



@login_required
@Administrador.route('/CrearUsuarios', methods=['GET', 'POST'])
def CrearUsuarios():
    """ Método vista para el registro de usuarios. """
    register_form = RegistrarUsuario()
    context = {
        'register_form': register_form
    }
    if register_form.validate_on_submit():
        user = get_user_by_username(register_form.username.data)
        if user is None:
        #Proceso para registrar usuario :V
            user_data = {
                'Rol':register_form.Rol.data,  
                'nombre':register_form.nombre.data,
                'apellido':register_form.apellido.data,    
                'email':register_form.email.data,   
                'cellphone':register_form.cellphone.data,   
                'username':register_form.username.data,    
                'password':register_form.password.data,  
            }

            registro_usuarios(user_data)
            user_model = UserModel(
                get_user_by_username(register_form.username.data)
            )
            login_user(user_model)
            flash("Registro Exitoso", category="info")
            return redirect(url_for("Administrador.CrearUsuarios"))

        else:
            flash("El usuario  ya existe en el sistema", category="warning")
        
            

    return render('Administrador/CrearUsuarios.html', **context)


@Administrador.route('/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    flash('Sesion Cerrada', category="info")
    return redirect(url_for('Autentificacion.Login'))