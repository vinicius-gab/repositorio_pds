from app import app, db
from app.models import Usuario


class UsuarioController:
    def salvar(formulario):
        usuario = Usuario()
        usuario.username = formulario["usuario"].data
        usuario.password = formulario["senha"].data
        usuario.email = formulario["email"].data
        db.session.add(usuario)
        db.session.commit()

        return True