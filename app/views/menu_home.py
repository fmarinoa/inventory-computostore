# views/menu_home.py

def mostrar_menu_home():
    while True:
        print("\n===== COMPUTOSTORE - MENÚ PRINCIPAL =====")
        print("1. Gestión de productos")
        print("2. Control y alertas de stock")
        print("3. Ver historial de movimientos")
        print("4. Salir del sistema")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            mostrar_menu_gestion_productos()
        elif opcion == "2":
            mostrar_menu_control_stock()
        elif opcion == "3":
            mostrar_menu_historial()
        elif opcion == "4":
            print("\nGracias por usar ComputoStore. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


def mostrar_menu_gestion_productos():
    print("\n--- GESTIÓN DE PRODUCTOS ---")
    print("1. Registrar nuevo producto")
    print("2. Listar productos")
    print("3. Modificar producto existente")
    print("4. Eliminar producto")
    print("5. Volver al menú principal")
    input("Presiona Enter para continuar...")


def mostrar_menu_control_stock():
    print("\n--- CONTROL Y ALERTAS DE STOCK ---")
    print("1. Ver productos con stock mínimo")
    print("2. Generar alerta de reabastecimiento")
    print("3. Volver al menú principal")
    input("Presiona Enter para continuar...")


def mostrar_menu_historial():
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    print("1. Ver historial completo")
    print("2. Filtrar historial por fecha o acción")
    print("3. Volver al menú principal")
    input("Presiona Enter para continuar...")

