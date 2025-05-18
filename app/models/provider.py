from app.models.product import Product


class Provider:
    def __init__(self, id:str, name: str, contact: str, phone: str, email: str, address: str):
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__products = []

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

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
    def products(self):
        return self.__products

    def __str__(self):
        return (
            f"Id: {self.id} ,Nombre: {self.__name}, Contacto: {self.__contact}, Teléfono: {self.__phone},"
            f" Email: {self.__email}, Dirección: {self.__address}, Productos: {len(self.products)}"
            f" ({', '.join([str(product) for product in self.products])})"
        )

    def add_product(self, product: Product):
        self.products.append(product)
        product.provider = self
        
    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            product.provider = None
            
    def show_info(self):
        return str(self)
    