from app.data.store import main_clients
from app.models.client import Client


def mostrar_menu_gestion_clientes():
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Registrar un nuevo cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente existente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            modificar_cliente()
        elif op == "4":
            eliminar_cliente()
        elif op == "5":
            break
        else:
            print("Opción no válida.")


def registrar_cliente():
    print("Registrar nuevo cliente")
    id = input("Ingrese el ID del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    email = input("Ingrese el email del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")

    cliente = Client(id, nombre, telefono, email, direccion)
    main_clients.append(cliente)

    print(f"Cliente {cliente.name} registrado con éxito.")


def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    
    if not main_clients:
        print("No hay clientes registrados.")
    else:
        for i, cliente in enumerate(main_clients, start=1):
            print(f"{i}. {str(cliente)}")

    print("--- FIN DE CLIENTES ---")


def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")

    if not main_clients:
        print("No hay clientes registrados.")
        return

    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    cliente_encontrado = buscar_cliente_por_id(id_cliente)

    if not cliente_encontrado:
        print("Cliente no encontrado.")
        return

    print(f"Cliente encontrado: {cliente_encontrado}")
    print("Ingrese los nuevos datos del cliente (deje en blanco para no modificar):")
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    telefono = input("Ingrese el nuevo teléfono del cliente: ")
    email = input("Ingrese el nuevo email del cliente: ")
    direccion = input("Ingrese la nueva dirección del cliente: ")

    if nombre:
        cliente_encontrado.name = nombre
    if telefono:
        cliente_encontrado.phone = telefono
    if email:
        cliente_encontrado.email = email
    if direccion:
        cliente_encontrado.address = direccion

    print(f"Cliente {cliente_encontrado.name} modificado con éxito.")


def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")

    if not main_clients:
        print("No hay clientes registrados.")
        return

    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    cliente_encontrado = buscar_cliente_por_id(id_cliente)

    if not cliente_encontrado:
        print("Cliente no encontrado.")
        return

    main_clients.remove(cliente_encontrado)
    print(f"Cliente {cliente_encontrado.name} eliminado con éxito.")

""" original
def buscar_cliente_por_id(id):
    for p in main_clients:
        if p.id_product == id: original
        if p.id == id:  #cambio agregado
            return p
    return None
"""
### agregado

def buscar_cliente_por_id(id):
    for cliente in main_clients:
        if cliente.client_id == id:
            return cliente