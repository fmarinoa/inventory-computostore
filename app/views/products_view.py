from datetime import datetime
from decimal import Decimal

from app.data.store import main_products
from app.models.product import ProductSoftware, ProductHardware
from app.utils.validators import ProductValidators


def mostrar_menu_gestion_productos():
    while True:
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Registrar nuevo producto")
        print("2. Listar productos")
        print("3. Modificar producto existente")
        print("4. Eliminar producto")
        print("5. Buscar producto por código")
        print("6. Volver al menú principal")

        op = input("Selecciona una opción (1-6): ")

        if op == "1":
            registrar_producto()
        elif op == "2":
            listar_productos()
        elif op == "3":
            modificar_producto()
        elif op == "4":
            eliminar_producto()
        elif op == "5":
            buscar_producto_por_codigo()
        elif op == "6":
            break
        else:
            print("Opción no válida.")


def buscar_producto_por_codigo():
    id_producto = input("Ingrese el ID del producto a buscar: ")
    producto_encontrado = _buscar_producto_por_id(id_producto)

    if producto_encontrado is None:
        print("Producto no encontrado.")
        return

    print(f"Producto encontrado: {producto_encontrado.get_product_info()}")


def eliminar_producto():
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    producto_encontrado = _buscar_producto_por_id(id_producto)

    if producto_encontrado is None:
        print("Producto no encontrado.")
        return

    main_products.remove(producto_encontrado)
    print(f"Producto {producto_encontrado.name} eliminado con éxito.")


def modificar_producto():
    id_producto = input("Ingrese el ID del producto a modificar: ")
    producto_encontrado = _buscar_producto_por_id(id_producto)

    if producto_encontrado is None:
        print("Producto no encontrado.")
        return

    print(f"Producto encontrado: {producto_encontrado.name}")

    nuevos_datos = _obtener_nuevos_datos_producto(producto_encontrado)
    _actualizar_producto(producto_encontrado, nuevos_datos)
    producto_encontrado.date_update = datetime.now()

    print(f"Producto modificado con éxito: {producto_encontrado.name}")


def _buscar_producto_por_id(id_producto):
    for p in main_products:
        if p.id_product == id_producto:
            return p
    return None


def _obtener_nuevos_datos_producto(producto):
    print("Ingrese los nuevos datos del producto (deje en blanco para no modificar):")
    nombre = input(f"Nombre ({producto.name}): ")
    descripcion = input(f"Descripción ({producto.description}): ")
    marca = input(f"Marca ({producto.brand}): ")
    modelo = input(f"Modelo ({producto.model}): ")
    numero_serie = input(f"Número de serie ({producto.serial_number}): ")
    stock = input(f"Stock ({producto.stock}): ")
    precio = input(f"Precio ({producto.price}): ")
    minimo_stock = input(f"Stock mínimo ({producto.minimum_stock}): ")

    stock = ProductValidators.validate_stock(stock) if stock else None
    precio = ProductValidators.validate_price(precio) if precio else None

    tipo_producto = 1 if isinstance(producto, ProductSoftware) else 2
    tipo_licencia = None
    ram = None
    almacenamiento = None
    procesador = None

    if tipo_producto == 1:
        tipo_licencia = input(f"Tipo de licencia ({producto.type_license}): ")
    else:
        ram = input(f"RAM ({producto.ram}): ")
        almacenamiento = input(f"Almacenamiento ({producto.storage}): ")
        procesador = input(f"Procesador ({producto.processor}): ")

    return {
        "nombre": nombre,
        "descripcion": descripcion,
        "marca": marca,
        "modelo": modelo,
        "numero_serie": numero_serie,
        "stock": stock,
        "precio": precio,
        "minimo_stock": minimo_stock,
        "tipo_producto": tipo_producto,
        "tipo_licencia": tipo_licencia,
        "ram": ram,
        "almacenamiento": almacenamiento,
        "procesador": procesador
    }


def _actualizar_producto(producto, datos):
    if datos["nombre"] is not None:
        producto.name = datos["nombre"]
    if datos["descripcion"] is not None:
        producto.description = datos["descripcion"]
    if datos["marca"] is not None:
        producto.brand = datos["marca"]
    if datos["modelo"] is not None:
        producto.model = datos["modelo"]
    if datos["numero_serie"] is not None:
        producto.serial_number = datos["numero_serie"]
    if datos["stock"] is not None:
        producto.stock = datos["stock"]
    if datos["precio"] is not None:
        producto.price = datos["precio"]
    if datos["minimo_stock"] is not None:
        producto.minimum_stock = datos["minimo_stock"]

    if datos["tipo_producto"] == 1 and datos["tipo_licencia"] is not None:
        producto.type_license = datos["tipo_licencia"]
    elif datos["tipo_producto"] == 2:
        if datos["ram"] is not None:
            producto.ram = datos["ram"]
        if datos["almacenamiento"] is not None:
            producto.storage = datos["almacenamiento"]
        if datos["procesador"] is not None:
            producto.processor = datos["procesador"]


def listar_productos():
    print("Listado de productos")
    for p in main_products:
        print(p)


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

    main_products.append(product)

    print(f"Producto {product.name} registrado con éxito.")
