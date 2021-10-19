#Ver que se creeen las tablas que hagamos :V
from .database import *

def create_db():
    #Metodo para la creacion de la base de datos 

    db.drop_all()
    db.create_all()

def init_db():
    #Metodo para inicializar nuestra base de datos :V
    create_db()
    #Usuario por defecto (admin)
    admin = User(
        nombre='Javier',
        apeliido='Moreno',
        email='morenofj@uninorte.edu.co',
        cellphone='3104207720',
        username='Javier',
        is_Admin=True,
        is_Docente=False,
        is_Estudiante=False,
    )
    admin.set_password("Adm1n**123")
    db.session.add(admin) 
    db.session.commit()  #Registrar Cambios