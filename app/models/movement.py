from datetime import datetime

from app.models.client import Client
from app.models.product import Product


class Movement:
    def __init__(self, product: Product, client: Client, amount: int):
        self.__product = product
        self.__client = client
        self.amount = amount
        self.date = datetime.now()
    
    @property
    def product(self):
        return self.__product    
    
    @product.setter
    def product(self, product: Product):
        self.__product = product
        
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, client: Client):
        self.__client = client        
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount