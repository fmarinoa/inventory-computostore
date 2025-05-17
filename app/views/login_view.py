from app.exceptions.auth_exceptions import IncorrectPasswordError, UserNotFoundError, UserInactiveError
from app.models.user import User
from app.views.menu_home import mostrar_menu_home


def login_view(user: User):
    print("\n--- Iniciar Sesión ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    # Aquí deberías validar el usuario con tu controlador real
    if not user.verify_user(username):
        raise UserNotFoundError()

    if not user.verify_password(password):
        raise IncorrectPasswordError()

    if not user.verify_status():
        raise UserInactiveError()

    mostrar_menu_home()
