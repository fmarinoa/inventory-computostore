from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal

from app.utils.validators import ProductValidators


class Product(ABC):
    def __init__(self, id_product: str, name: str, description: str, brand: str, model: str, serial_number: str,
                 stock: int, price: Decimal, type_product: str, minimum_stock: int = 0):
        self.__id_product = id_product
        self.__brand = brand
        self.__model = model
        self.__serial_number = serial_number
        self.__name = name
        self.__description = description
        self.__stock = stock
        self.__price = price
        self.__type_product = type_product
        self.__minimum_stock = minimum_stock
        self.__date_update = datetime.now()
        self.__provider = None
        self.__category = None
        self.__purchases = []

    @property
    def id_product(self):
        return self.__id_product

    @id_product.setter
    def id_product(self, id_product: str):
        self.__id_product = id_product

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def serial_number(self):
        return self.__serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        self.__serial_number = serial_number

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def type_product(self):
        return self.__type_product

    @type_product.setter
    def type_product(self, type_product: str):
        self.__type_product = type_product

    @property
    def minimum_stock(self):
        return self.__minimum_stock

    @minimum_stock.setter
    def minimum_stock(self, minimum_stock: int):
        self.__minimum_stock = minimum_stock

    @property
    def date_update(self):
        return self.__date_update

    @date_update.setter
    def date_update(self, date_update: str):
        self.__date_update = date_update

    @property
    def provider(self):
        return self.__provider
    
    @provider.setter
    def provider(self, provider):
        self.__provider = provider
        
    @property
    def category(self):
        return self.__category
    
    @category.setter 
    def category(self, category):
        self.__category = category
        
    @property
    def purchases(self):
        return self.__purchases
    
    @purchases.setter
    def purchases(self, purchases):
        self.__purchases = purchases

    def __str__(self):
        date_str = self.date_update.strftime("%d/%m/%Y %H:%M:%S") if isinstance(self.date_update, datetime) else str(self.date_update)
        return (
            f"ID: {self.id_product}, Nombre: {self.name}, Descripción: {self.description}, "
            f"Marca: {self.brand}, Modelo: {self.model}, Número de serie: {self.serial_number}, "
            f"Stock: {self.stock}, Precio: {self.price}, Tipo de producto: {self.type_product}, "
            f"Stock mínimo: {self.minimum_stock}, Última actualización: {date_str}, Proveedor: {self.provider}, "
            f"Categoría: {self.category}, Compras: {len(self.purchases)}"
            f" ({', '.join([str(purchase) for purchase in self.purchases])})"
        )

    @abstractmethod
    def get_product_info(self):
        pass

    def add_stock(self, amount: int):
        amount = ProductValidators.validate_stock(amount)
        self.__stock += amount
        self.__date_update = datetime.now()

    def remove_stock(self, amount: int):
        amount = ProductValidators.validate_stock(amount)
        if self.__stock - amount < 0:
            raise ValueError("No hay suficiente stock para realizar esta operación.")

        self.__stock -= amount
        self.__date_update = datetime.now()

    def update_stock(self, stock: int):
        stock = ProductValidators.validate_stock(stock)
        self.__stock = stock
        self.__date_update = datetime.now()

    def assign_discount(self, discount):
        if not isinstance(discount, (int, float)):
            raise ValueError("El descuento debe ser un número.")

        self.__price -= ProductValidators.validate_price(Decimal(discount / 100) * self.price)
        self.__date_update = datetime.now()


class ProductSoftware(Product):
    def __init__(self, id_product: str, name: str, description: str, brand: str, model: str, serial_number: str,
                 stock: int, price: Decimal, minimum_stock: int, type_license: str):
        super().__init__(id_product, name, description, brand, model, serial_number, stock, price, "software",
                         minimum_stock)
        self.__type_license = type_license

    @property
    def type_license(self):
        return self.__type_license

    @type_license.setter
    def type_license(self, type_license: str):
        self.__type_license = type_license

    def get_product_info(self):
        return str(self) + f", Tipo de licencia: {self.__type_license}"


class ProductHardware(Product):
    def __init__(self, id_product: str, name: str, description: str, brand: str, model: str, serial_number: str,
                 stock: int, price: Decimal, minimum_stock: int, ram: str, storage: str, processor: str):
        super().__init__(id_product, name, description, brand, model, serial_number, stock, price, "hardware",
                         minimum_stock)
        self.__ram = ram
        self.__storage = storage
        self.__processor = processor

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram: str):
        self.__ram = ram

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, storage: str):
        self.__storage = storage

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, processor: str):
        self.__processor = processor

    def get_product_info(self):
        return str(self) + f", RAM: {self.ram}, Almacenamiento: {self.storage}, Procesador: {self.processor}"
