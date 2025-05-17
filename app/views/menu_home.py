def mostrar_menu_home():
    while True:
        print("\n===== COMPUTOSTORE - MENÚ PRINCIPAL =====")
        print("1. Gestión de productos")
        print("2. Control y alertas de stock")
        print("3. Ver historial de movimientos")
        print("4. Gestión de categorías")
        print("5. Gestión de proveedores")
        print("6. Salir del sistema")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            mostrar_menu_gestion_productos()
        elif opcion == "2":
            mostrar_menu_control_stock()
        elif opcion == "3":
            mostrar_menu_historial()
        elif opcion == "4":
            mostrar_menu_gestion_categorias()
        elif opcion == "5":
            mostrar_menu_gestion_proveedores()
        elif opcion == "6":
            print("\nGracias por usar ComputoStore. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


# Menús existentes

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


# Nuevos menús

def mostrar_menu_gestion_categorias():
    while True:
        print("\n--- GESTIÓN DE CATEGORÍAS ---")
        print("1. Ingresar nueva categoría")
        print("2. Mostrar descripción de una categoría")
        print("3. Listar todas las categorías")
        print("4. Modificar una categoría")
        print("5. Eliminar una categoría")
        print("6. Volver al menú principal")

        op = input("Selecciona una opción: ")

        if op == "6":
            break
        else:
            print("Opción no implementada aún.")
    input("Presiona Enter para continuar...")


def mostrar_menu_gestion_proveedores():
    while True:
        print("\n--- GESTIÓN DE PROVEEDORES ---")
        print("1. Registrar nuevo proveedor")
        print("2. Buscar proveedor por nombre")
        print("3. Listar todos los proveedores")
        print("4. Modificar datos de un proveedor")
        print("5. Eliminar proveedor")
        print("6. Volver al menú principal")

        op = input("Selecciona una opción: ")

        if op == "6":
            break
        else:
            print("Opción no implementada aún.")
    input("Presiona Enter para continuar...")
