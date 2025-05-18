class Category:
    def __init__(self, id: str, name: str, description: str, products: list = None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__products = products if products is not None else []

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
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description: str):
        self.__description = description
        
    @property
    def products(self):
        return self.__products
    
    def __str__(self):
        return (
            f"Id: {self.id}, Nombre: {self.name}, Descripción: {self.description}, Productos: {len(self.products)}"
            f" ({', '.join([str(product.name) for product in self.products])})"
        )
    
    def add_product(self, product):
        self.__products.append(product)
        product.category = self
        
    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
            product.category = None
            
    def show_info(self):
        return str(self)
    