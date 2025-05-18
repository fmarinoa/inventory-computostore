#from app.models.client import Client
from app.models.client import Client
from app.models.category import Category
from app.models.provider import Provider
from app.models.product import Product
from app.models.movement import Movement
from app.models.product import ProductHardware, ProductSoftware
from decimal import Decimal

cliente1 = Client("CLI001", "FRANCO MARIÑO", "987654321", "franco@gmail.com", "Av. La Marina 2512")
cliente2 = Client("CLI002", "EDSON AQUISE", "963258741", "edson@gmail.com", "Av. La Marina 2531")
cliente3 = Client("CLI003", "HENRY MONDRAGON", "951357852", "henry@gmail.com", "Av. La Marina 2122")
main_clients = [cliente1, cliente2, cliente3]


# === CATEGORÍAS ===
categoria1 = Category("CAT001", "Hardware", "Equipos y componentes informáticos")
categoria2 = Category("CAT002", "Software", "Licencias y programas informáticos")
main_categories = [categoria1, categoria2]

# === PROVEEDORES ===
proveedor1 = Provider(
    id="PROV001",
    name="Tecnosac S.A.",
    contact="Carlos Mendoza",
    phone="987654321",
    email="ventas@tecnosac.com",
    address="Av. Javier Prado 1001"
)

proveedor2 = Provider(
    id="PROV002",
    name="SoftPerú SAC",
    contact="Ana Rojas",
    phone="963852741",
    email="soporte@softperu.com.pe",
    address="Av. Universitaria 1200"
)

main_providers = [proveedor1, proveedor2]

# === PRODUCTOS ===
producto1 = ProductHardware(
    id_product="PROD001",
    name="Laptop HP",
    description="Equipos de cómputo",
    brand="HP",
    model="Pavilion 15",
    serial_number="SN123456789",
    stock=10,
    price=Decimal("1200.00"),
    minimum_stock=5,
    ram="16GB",
    storage="512GB SSD",
    processor="Intel i7"
)

producto2 = ProductSoftware(
    id_product="PROD002",
    name="Microsoft Office 365",
    description="Suite ofimática",
    brand="Microsoft",
    model="Office 365",
    serial_number="SN987654321",
    stock=50,
    price=Decimal("150.00"),
    minimum_stock=10,
    type_license="Suscripción anual"
)

producto3 = ProductHardware(
    id_product="PROD003",
    name="Smartphone Samsung Galaxy S25",
    description="Teléfono inteligente de alta gama",
    brand="Samsung",
    model="Galaxy S25",
    serial_number="SN987000123",
    stock=25,
    price=Decimal("900.00"),
    minimum_stock=5,
    ram="12GB",
    storage="256GB",
    processor="Snapdragon 8 Gen 3"
)

main_products = [producto1, producto2, producto3]

# === MOVIMIENTOS ===
movimiento1 = Movement(
    product=producto1,   # Producto creado antes
    client=cliente1,     # Cliente ya definido
    amount=5             # Cantidad vendida
)

movimiento2 = Movement(
    product=producto2,
    client=cliente2,
    amount=2
)

movimiento3 = Movement(
    product=producto3,
    client=cliente3,
    amount=1
)
main_movements = [movimiento1, movimiento2, movimiento3]





"""
main_products = []
main_movements = []
main_categories = []
main_providers = []
"""