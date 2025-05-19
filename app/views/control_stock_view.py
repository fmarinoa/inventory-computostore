from app.data.store import main_products


def mostrar_menu_control_stock():
    while True:
        print("\n--- CONTROL Y ALERTAS DE STOCK ---")
        lista_productos = obtener_productos_bajo_stock()

        mostrar_productos_bajo_stock(lista_productos)

        print("\n1. Actualizar stock de productos")
        print("2. Volver al menú principal")

        opcion = input("Selecciona una opción (1-2): ")
        if opcion == "1":
            actualizar_stock_productos(lista_productos)
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")


def obtener_productos_bajo_stock():
    return [p for p in main_products if p.stock <= p.minimum_stock]


def mostrar_productos_bajo_stock(lista_productos):
    if not lista_productos:
        print("No hay productos con stock bajo.")
    else:
        print("Productos con stock bajo:")
        for i, producto in enumerate(lista_productos, start=1):
            print(
                f"{i}. {producto.name} - Stock: {producto.stock} - Stock mínimo: {producto.minimum_stock} - Precio:"
                f" {producto.price} - Proveedor: {producto.provider.name} - Categoría: {producto.category.name}")


def actualizar_stock_productos(lista_productos):
    if not lista_productos:
        print("No hay productos con stock bajo para actualizar.")
        return

    print("\n--- ACTUALIZAR STOCK DE PRODUCTOS ---")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. {producto.name} - Stock actual: {producto.stock}")

    opcion = input("Selecciona el número del producto a actualizar (o 'q' para salir): ")

    if opcion.lower() == 'q':
        return

    try:
        index = int(opcion) - 1
        if index < 0 or index >= len(lista_productos):
            raise ValueError("Número de producto no válido.")

        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        lista_productos[index].stock = nuevo_stock
        print(f"Stock actualizado para {lista_productos[index].name}. Nuevo stock: {nuevo_stock}")
    except ValueError as e:
        print(f"Error: {e}")
