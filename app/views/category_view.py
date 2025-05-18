from app.data.store import main_categories
from app.models.category import Category
from app.views.products_view import buscar_producto_por_id


def mostrar_menu_gestion_categorias():
    while True:
        print("\n--- GESTIÓN DE CATEGORÍAS ---")
        print("1. Registrar una nueva categoría")
        print("2. Listar categorías")
        print("3. Modificar categoría existente")
        print("4. Eliminar categoría")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_categoria()
        elif op == "2":
            listar_categorias()
        elif op == "3":
            modificar_categoria()
        elif op == "4":
            eliminar_categoria()
        elif op == "5":
            break
        else:
            print("Opción no válida.")


def registrar_categoria():
    print("Registrar nueva categoría")
    id = input("Ingrese el ID de la categoría: ")
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")

    categoria = Category(id, nombre, descripcion)
    main_categories.append(categoria)

    agregar_productos(categoria)

    print(f"Categoría {categoria.name} registrado con éxito.")


def listar_categorias():
    print("\n--- LISTA DE CATEGORÍAS ---")
    if not main_categories:
        print("No hay categorías registradas.")
    else:
        for i, categoria in enumerate(main_categories, start=1):
            print(f"{i}. {categoria.show_info()}")
    print("--- FIN DE CATEGORÍAS ---")


def modificar_categoria():
    print("\n--- MODIFICAR CATEGORÍA ---")

    if not main_categories:
        print("No hay categorías registradas.")
        return

    id_categoria = input("Ingrese el ID de la categoría a modificar: ")
    categoria_encontrada = buscar_categoria_por_id(id_categoria)

    if categoria_encontrada is None:
        print("Categoría no encontrada.")
        return

    print(f"Categoría encontrada: {categoria_encontrada.name} - Descripción: {categoria_encontrada.description}")
    print("Ingrese los nuevos datos de la categoría (deje en blanco para no modificar):")

    nuevo_nombre = input(f"Nuevo nombre (actual: {categoria_encontrada.name}): ")
    nueva_descripcion = input(f"Nueva descripción (actual: {categoria_encontrada.description}): ")

    if nuevo_nombre:
        categoria_encontrada.name = nuevo_nombre

    if nueva_descripcion:
        categoria_encontrada.description = nueva_descripcion

    agregar_productos(categoria_encontrada)
    remover_productos(categoria_encontrada)


def agregar_productos(categoria: Category):
    if input("Desea agregar productos a la categoria? (s/n): ") == 's':
        while True:
            id_producto = input("Ingrese el ID del producto a agregar (o 'q' para salir): ")
            if id_producto.lower() == 'q':
                break
            producto_encontrado = buscar_producto_por_id(id_producto)
            if producto_encontrado:
                categoria.add_product(producto_encontrado)
            else:
                print("Producto no encontrado.")


def remover_productos(categoria: Category):
    if input("Desea quitar productos a la categoria? (s/n): ") == 's':
        while True:
            id_producto = input("Ingrese el ID del producto a remover (o 'q' para salir): ")
            if id_producto.lower() == 'q':
                break
            producto_encontrado = buscar_producto_por_id(id_producto)
            if producto_encontrado:
                categoria.remove_product(producto_encontrado)
            else:
                print("Producto no encontrado.")


def buscar_categoria_por_id(id):
    for c in main_categories:
        if c.id == id:
            return c
    return None


def eliminar_categoria():
    print("\n--- ELIMINAR CATEGORÍA ---")

    if not main_categories:
        print("No hay categorías registradas.")
        return

    id_categoria = input("Ingrese el ID de la categoría a eliminar: ")
    categoria_encontrada = buscar_categoria_por_id(id_categoria)

    if categoria_encontrada is None:
        print("Categoría no encontrada.")
        return

    main_categories.remove(categoria_encontrada)
    print(f"Categoría {categoria_encontrada.name} eliminada con éxito.")
