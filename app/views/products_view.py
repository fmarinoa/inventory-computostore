from decimal import Decimal

from app.models.product import ProductSoftware, ProductHardware
from app.utils.validators import ProductValidators
from main import products


def mostrar_menu_gestion_productos():
    while True:
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Registrar nuevo producto")
        print("2. Listar productos")
        print("3. Modificar producto existente")
        print("4. Eliminar producto")
        print("5. Buscar producto por código")
        print("6. Volver al menú principal")
        op = input("Selecciona una opción: ")

        if op == "1":
            registrar_producto()

        elif op == "6":
            break
        else:
            print("Opción no válida.")


def registrar_producto():
    print("Registrar nuevo producto")
    print("1. Producto de tipo Software")
    print("2. Producto de tipo Hardware")
    tipo_producto = int(input("Selecciona el tipo de producto (1 o 2): "))

    if tipo_producto != 1 and tipo_producto != 2:
        print("Opción no válida.")
        return

    print(f"Registrar producto de tipo {'Software' if tipo_producto == 1 else 'Hardware'}")

    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    marca = input("Ingrese la marca del producto: ")
    modelo = input("Ingrese el modelo del producto: ")
    numero_serie = input("Ingrese el número de serie del producto: ")
    stock = input("Ingrese la cantidad de stock del producto: ")
    precio = input("Ingrese el precio del producto: ")
    minimo_stock = input("Ingrese el stock mínimo del producto: ")

    precio = ProductValidators.validate_price(precio)

    product = None

    if tipo_producto == 1:
        tipo_licencia = input("Ingrese el tipo de licencia del software: ")

        product = ProductSoftware(
            id_product=id_producto,
            name=nombre,
            description=descripcion,
            brand=marca,
            model=modelo,
            serial_number=numero_serie,
            stock=int(stock),
            price=Decimal(precio),
            minimum_stock=int(minimo_stock),
            type_license=tipo_licencia
        )
    elif tipo_producto == 2:
        ram = input("Ingrese la cantidad de RAM del hardware: ")
        almacenamiento = input("Ingrese la capacidad de almacenamiento del hardware: ")
        procesador = input("Ingrese el tipo de procesador del hardware: ")
        product = ProductHardware(
            id_product=id_producto,
            name=nombre,
            description=descripcion,
            brand=marca,
            model=modelo,
            serial_number=numero_serie,
            stock=int(stock),
            price=Decimal(precio),
            minimum_stock=int(minimo_stock),
            ram=ram,
            storage=almacenamiento,
            processor=procesador
        )

    products.append(product)

    print(f"Producto {product.name} registrado con éxito.")
