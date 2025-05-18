from app.data.store import main_providers
from app.models.provider import Provider
from app.views.products_view import buscar_producto_por_id


def mostrar_menu_gestion_proveedores():
    while True:
        print("\n--- GESTIÓN DE PROVEEDORES ---")
        print("1. Registrar un nuevo proveedor")
        print("2. Listar proveedores")
        print("3. Modificar proveedor existente")
        print("4. Eliminar proveedor")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_proveedor()
        elif op == "2":
            listar_proveedores()
        elif op == "3":
            modificar_proveedor()
        elif op == "4":
            eliminar_proveedor()
        elif op == "5":
            break
        else:
            print("Opción no válida.")


def registrar_proveedor():
    print("Registrar nuevo proveedor")
    id = input("Ingrese el ID del proveedor: ")
    nombre = input("Ingrese el nombre del proveedor: ")
    contacto = input("Ingrese el contacto del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    email = input("Ingrese el email del proveedor: ")
    direccion = input("Ingrese la dirección del proveedor: ")

    proveedor = Provider(id, nombre, contacto, telefono, email, direccion)
    main_providers.append(proveedor)

    agregar_productos(proveedor)

    print(f"Proveedor {proveedor.name} registrado con éxito.")


def agregar_productos(proveedor: Provider):
    print(f"Agregar productos al proveedor {proveedor.name}")
    while True:
        id_producto = input("Ingrese el ID del producto (o 'q' para salir): ")
        if id_producto.lower() == 'q':
            break
        producto = buscar_producto_por_id(id_producto)
        if producto:
            proveedor.add_product(producto)
            print(f"Producto {producto.name} agregado al proveedor {proveedor.name}.")
        else:
            print("Producto no encontrado.")


def listar_proveedores():
    print("\n--- LISTA DE PROVEEDORES ---")
    if not main_providers:
        print("No hay proveedores registrados.")
    else:
        for i, proveedor in enumerate(main_providers, start=1):
            print(f"{i}. {proveedor.show_info()}")


def buscar_proveedor_por_id(id_proveedor):
    for proveedor in main_providers:
        if proveedor.id == id_proveedor:
            return proveedor
    return None


def modificar_proveedor():
    print("\n--- MODIFICAR PROVEEDOR ---")

    if not main_providers:
        print("No hay proveedores registrados.")
        return

    id_proveedor = input("Ingrese el ID del proveedor a modificar: ")
    proveedor_encontrado = buscar_proveedor_por_id(id_proveedor)

    if proveedor_encontrado is None:
        print("Proveedor no encontrado.")
        return

    print(f"Proveedor encontrado: {proveedor_encontrado.name} - Contacto: {proveedor_encontrado.contact}")
    print("Ingrese los nuevos datos del proveedor (deje en blanco para no modificar):")

    nuevo_nombre = input(f"Nuevo nombre (actual: {proveedor_encontrado.name}): ")
    nuevo_contacto = input(f"Nuevo contacto (actual: {proveedor_encontrado.contact}): ")
    nuevo_telefono = input(f"Nuevo teléfono (actual: {proveedor_encontrado.phone}): ")
    nuevo_email = input(f"Nuevo email (actual: {proveedor_encontrado.email}): ")
    nueva_direccion = input(f"Nueva dirección (actual: {proveedor_encontrado.address}): ")

    if nuevo_nombre:
        proveedor_encontrado.name = nuevo_nombre
    if nuevo_contacto:
        proveedor_encontrado.contact = nuevo_contacto
    if nuevo_telefono:
        proveedor_encontrado.phone = nuevo_telefono
    if nuevo_email:
        proveedor_encontrado.email = nuevo_email
    if nueva_direccion:
        proveedor_encontrado.address = nueva_direccion

    agregar_productos(proveedor_encontrado)
    remover_productos(proveedor_encontrado)

    print(f"Proveedor {proveedor_encontrado.name} modificado con éxito.")


def remover_productos(proveedor: Provider):
    if input("Desea remover productos del proveedor? (s/n): ") == 's':
        while True:
            id_producto = input("Ingrese el ID del producto a remover (o 'q' para salir): ")
            if id_producto.lower() == 'q':
                break
            producto_encontrado = buscar_producto_por_id(id_producto)
            if producto_encontrado:
                proveedor.remove_product(producto_encontrado)
                print(f"Producto {producto_encontrado.name} removido del proveedor {proveedor.name}.")
            else:
                print("Producto no encontrado.")


def eliminar_proveedor():
    print("\n--- ELIMINAR PROVEEDOR ---")

    if not main_providers:
        print("No hay proveedores registrados.")
        return

    id_proveedor = input("Ingrese el ID del proveedor a eliminar: ")
    proveedor_encontrado = buscar_proveedor_por_id(id_proveedor)

    if proveedor_encontrado is None:
        print("Proveedor no encontrado.")
        return

    main_providers.remove(proveedor_encontrado)
    print(f"Proveedor {proveedor_encontrado.name} eliminado con éxito.")
