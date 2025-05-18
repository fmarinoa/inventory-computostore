from app.data.store import main_clients


def buscar_cliente_por_id(id):
    for p in main_clients:
        if p.id_product == id:
            return p
    return None
