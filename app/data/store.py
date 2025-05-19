from decimal import Decimal

from app.models.category import Category
from app.models.client import Client
from app.models.product import ProductHardware, ProductSoftware
from app.models.provider import Provider

# === CLIENTES ===
cliente1 = Client("CLI001", "FRANCO MARIÑO", "987654321", "franco@gmail.com", "Av. La Marina 2512")
cliente2 = Client("CLI002", "EDSON AQUISE", "963258741", "edson@gmail.com", "Av. La Marina 2531")
cliente3 = Client("CLI003", "HENRY MONDRAGON", "951357852", "henry@gmail.com", "Av. La Marina 2122")
main_clients = [cliente1, cliente2, cliente3]

# === CATEGORÍAS ===
categoria1 = Category("CAT001", "Laptops", "Laptops y perifericos")
categoria2 = Category("CAT002", "Celulares", "Celulares de todas las gamas")
categoria3 = Category("CAT002", "Licencias", "Licencias y programas informáticos")
main_categories = [categoria1, categoria2, categoria3]

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
    stock=9,
    price=Decimal("1200.00"),
    minimum_stock=10,
    ram="16GB",
    storage="512GB SSD",
    processor="Intel i7"
)
categoria1.add_product(producto1)
proveedor1.add_product(producto1)

producto2 = ProductSoftware(
    id_product="PROD002",
    name="Microsoft Office 365",
    description="Suite ofimática",
    brand="Microsoft",
    model="Office 365",
    serial_number="SN987654321",
    stock=100,
    price=Decimal("150.00"),
    minimum_stock=20,
    type_license="Suscripción anual"
)
categoria3.add_product(producto2)
proveedor1.add_product(producto2)

producto3 = ProductHardware(
    id_product="PROD003",
    name="Smartphone Samsung Galaxy S25",
    description="Teléfono inteligente de alta gama",
    brand="Samsung",
    model="Galaxy S25",
    serial_number="SN987000123",
    stock=55,
    price=Decimal("900.00"),
    minimum_stock=50,
    ram="12GB",
    storage="256GB",
    processor="Snapdragon 8 Gen 3"
)
categoria2.add_product(producto3)
proveedor2.add_product(producto3)

main_products = [producto1, producto2, producto3]

# === MOVIMIENTOS ===
main_movements = []
cliente1.purchase(producto1, 5)
cliente2.purchase(producto2, 2)
cliente3.purchase(producto3, 1)
