from app.exceptions.auth_exceptions import AuthenticationError
from app.models.user import User
from app.views.login_view import login_view
from app.models.client import Client

def main_menu(user: User):
    while True:
        print("\n=== Inventario de Productos ===")
        print("1. Iniciar Sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                login_view(user)
            except AuthenticationError as e:
                print(e)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    user = User("admin", "admin123", "Administrador", "admin@gmail.com", "admin")

    main_menu(user)
