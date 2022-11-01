# To make a variable or method private you can just add two underscores to it
# Abstract classes are used to hide data and methods from the user, 
# it cannot be instantiated and can only be accessed via inheritance
# Abstract classes are used to create a template for other classes to follow

from abc import ABC, abstractmethod
# decorator is used to add meta data to a function

class Product:
    id = 0
    name = ''
    description = ''
    type = ''
    amount = 0.0
    image = ''
    discount = 0.0

    def __init__(self, id, name, description, type, amount, image, discount):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.amount = amount
        self.image = image
        self.discount = discount

class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product: Product):
        pass
    
    @abstractmethod
    def edit_product(self, id):
        pass
    
    @abstractmethod
    def get_product_by_id(self, id):
        pass
    
    @abstractmethod
    def upload_product_image(self, image):
        pass

    @abstractmethod
    def delete_product(self, id):
        pass

class ProductManager(ProductAbstract):
    product = {}

    def __init__(self, product: Product):
        self.product = product

    def create_product(self):
        print(f'{self.product.name} has been created')

    def edit_product(self):
        print(f'Product with id - {self.product.id} has been edited')

    def get_product_by_id(self):
        print('Product with id: ' + str(self.product.id))
    
    def upload_product_image(self):
        print('Product image has been uploaded - imagepath: ' + self.product.image)
    
    def delete_product(self):
        print('Product has been deleted ' + str(self.product.id))

product = Product(1, 'Paracetamol', 'Take it to relieve your headache', 'Medication', 100.00, 'https://cdn.shopify.com/s/files/1/0470/8800/9366/products/PARA025___L_600x600.jpg?v=1610442948', 0.00)

product_manager = ProductManager(product)
product_manager.create_product()
product_manager.edit_product()
product_manager.get_product_by_id()
product_manager.upload_product_image()
product_manager.delete_product()