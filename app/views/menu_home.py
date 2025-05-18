from app.utils.console_util import limpiar_pantalla
from app.views.category_view import mostrar_menu_gestion_categorias
from app.views.control_stock_view import mostrar_menu_control_stock
from app.views.movement_purchase_view import mostrar_menu_gestion_movimientos_compras
from app.views.products_view import mostrar_menu_gestion_productos


def mostrar_menu_home():
    while True:
        limpiar_pantalla()  # se agrego
        print("\n===== COMPUTOSTORE - MENÚ PRINCIPAL =====")
        print("1. Gestión de productos")
        print("2. Control y alertas de stock")
        print("3. Gestión de movimientos/compras")
        print("4. Gestión de categorías")
        print("5. Gestión de proveedores")
        print("6. Gestión de clientes")
        print("7. Salir del sistema")

        opcion = input("Selecciona un opción (1-7): ")

        limpiar_pantalla()  # se agrego
        if opcion == "1":
            mostrar_menu_gestion_productos()
        elif opcion == "2":
            mostrar_menu_control_stock()
        elif opcion == "3":
            mostrar_menu_gestion_movimientos_compras()
        elif opcion == "4":
            mostrar_menu_gestion_categorias()
        # elif opcion == "5":
        #     mostrar_menu_gestion_proveedores()
        # elif opcion == "6":
        #     mostrar_menu_gestion_clientes()
        elif opcion == "7":
            print("\nGracias por usar ComputoStore. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")
