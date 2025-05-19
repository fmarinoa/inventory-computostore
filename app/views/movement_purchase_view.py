from app.data.store import main_clients
from app.views.client_view import buscar_cliente_por_id
from app.views.products_view import buscar_producto_por_id


def mostrar_menu_gestion_movimientos_compras():
    while True:
        print("\n--- GESTIÓN MOVIMIENTOS/COMPRAS ---")
        print("1. Registrar nuevo compra")
        print("2. Listar movimientos")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción (1-3): ")
        if opcion == "1":
            registrar_compra()
        elif opcion == "2":
            mostar_movimientos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def registrar_compra():
    try:
        id_producto = input("Ingrese el ID del producto a comprar: ")
        producto_encontrado = buscar_producto_por_id(id_producto)
        if producto_encontrado is None:
            print("Producto no encontrado.")
            return

        id_cliente = input("Ingrese el ID del cliente: ")
        cliente_encontrado = buscar_cliente_por_id(id_cliente)
        if cliente_encontrado is None:
            print("Producto no encontrado.")
            return

        cantidad = int(input("Ingrese la cantidad a comprar: "))
        if cantidad <= 0:
            print("Cantidad no válida.")
            return

        cliente_encontrado.purchase(producto_encontrado, cantidad)
        print(f"Compra registrada: {cliente_encontrado.name} compró {cantidad} unidades de {producto_encontrado.name}.")
    except Exception as e:
        print(f"Error: {e}")


def mostar_movimientos():
    print("\n--- LISTA DE MOVIMIENTOS ---")
    for cliente in main_clients:
        print(f"Cliente: {cliente.name}")
        for movimiento in cliente.purchases:
            # print(f"  Producto: {movimiento['product'].name}, Cantidad: {movimiento['amount']}")  se esta cambiando
            print(f"  Producto: {movimiento.product.name}, Cantidad: {movimiento.amount}")

    print("\n--- FIN DE MOVIMIENTOS ---")
