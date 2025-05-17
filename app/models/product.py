from datetime import datetime
from decimal import Decimal
from abc import ABC

class Product(ABC):
    def __init__(self, product_code: str, brand: str, model: str, serial_number: str, name: str, description: str,
                 stock: int, price: Decimal, date_creation: datetime = None):
        self.__product_code = product_code
        self.__brand = brand
        self.__model = model
        self.__serial_number = serial_number
        self.__name = name
        self.__description = description
        self.__stock = stock
        self.__price = price
        self.__date_update = datetime.now()
        self.__date_creation = date_creation

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code: str):
        self.__product_code = product_code

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
    def date_update(self):
        return self.__date_update

    @date_update.setter
    def date_update(self, date_update: str):
        self.__date_update = date_update

    @property
    def date_creation(self):
        return self.__date_creation

    @date_creation.setter
    def date_creation(self, date_creation: str):
        self.__date_creation = date_creation
