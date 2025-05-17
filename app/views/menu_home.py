from app.views.products_view import mostrar_menu_gestion_productos


def mostrar_menu_home():
    while True:
        print("\n===== COMPUTOSTORE - MENÚ PRINCIPAL =====")
        print("1. Gestión de productos")
        print("2. Control y alertas de stock")
        print("3. Ver historial de movimientos")
        print("4. Gestión de categorías")
        print("5. Gestión de proveedores")
        print("6. Gestión de clientes")
        print("7. Gestión de usuarios")
        print("8. Salir del sistema")

        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            mostrar_menu_gestion_productos()
        # elif opcion == "2":
        #     mostrar_menu_control_stock()
        # elif opcion == "3":
        #     mostrar_menu_historial()
        # elif opcion == "4":
        #     mostrar_menu_gestion_categorias()
        # elif opcion == "5":
        #     mostrar_menu_gestion_proveedores()
        # elif opcion == "6":
        #     mostrar_menu_gestion_clientes()
        # elif opcion == "7":
        #     mostrar_menu_gestion_usuarios()
        elif opcion == "8":
            print("\nGracias por usar ComputoStore. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

