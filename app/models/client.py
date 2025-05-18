from datetime import datetime

from app.models.product import Product


class Client:
    def __init__(self, client_id: str, name: str, phone: str, email: str, address: str):
        self.__client_id = client_id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__purchases = []

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id: str):
        self.__client_id = client_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def purchases(self):
        return self.__purchases

    def __str__(self):
        return (
            f"ID: {self.client_id}, Nombre: {self.name}, Teléfono: {self.phone}, Email: {self.email},"
            f" Dirección: {self.address}, Compras: {len(self.purchases)}"
            f" ({', '.join([str(purchase) for purchase in self.purchases])})"
        )

    def purchase(self, product: Product, quantity: int):
        from app.data.store import main_movements
        from app.models.movement import Movement

        if quantity > product.stock:
            raise ValueError("No hay suficiente stock disponible.")

        movement = Movement(product, self, quantity)
        self.purchases.append(movement)
        product.purchases.append(movement)
        product.remove_stock(quantity)
        product.date_update = datetime.now()
        main_movements.append(movement)
