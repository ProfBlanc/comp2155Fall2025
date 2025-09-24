"""
Create a checkout/purchases system

Product
    barcode
    name
    price

Store
    name
    inventory: list[Products]

PurchaseItem
    Product
    quantity

Purchase
    list[PurchaseItems]
    checkout(payment_method)

"""
class ValidationName:
    def __init__(self, name):
        self.name = name
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 2:
            self.__name = value
        else: raise ValueError("Invalid Name")

class Product(ValidationName):
    def __init__(self, barcode, name, price):
        super().__init__(name)
        self.barcode = barcode
        self.price = price
    @property
    def barcode(self): return self.__barcode
    @barcode.setter
    def barcode(self, value):
        if isinstance(value, int) and len(str(value)) >= 5:
            self.__barcode = value
        else: raise ValueError("Invalid barcode")
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__price = value
        else: raise ValueError("Invalid price")
    def __str__(self):
        return f"Product Barcode={self.barcode}, Product Name={self.name}, Product Price={self.price}"

class Store(ValidationName):
    def __init__(self, name):
        super().__init__(name)
        self.__inventory = list()
    def add_product(self, p: Product):
        if not isinstance(p, Product):
            raise TypeError("Not a product")
        self.__inventory.append(p)
    # create another method that allows user to add Product by inputting name, barcode, price
    def display_inventory(self):
        output = ""
        for p in self.__inventory:
            output += str(p) + "\n"
        return output

class PurchaseItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    @property
    def product(self): return self.__product
    @product.setter
    def product(self, value):
        if not isinstance(value, Product): raise ValueError("Invalid Product")
        self.__product = value
    @property
    def quantity(self): return self.__quantity
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 1: raise ValueError("Invalid Quantity")
        self.__quantity = value
    def __str__(self): return f"{self.product}, Quantity={self.quantity}"

class Purchase:
    def __init__(self):
        self.__items = list()
    def add_to_cart(self, purchase_item):
        if not isinstance(purchase_item, PurchaseItem): raise TypeError("Invalid data type")
        self.__items.append(purchase_item)
    def checkout(self, payment_type):
        if payment_type.lower() not in "visa,debit,cash".split(","): raise ValueError("Invalid payment type")
        if len(self.__items) == 0: raise ValueError("No items purchased")
        output = ""
        total = 0
        for item in self.__items:
            total += item.product.price * item.quantity
            output += str(item) + "\n"
        output += f"Grand Total = {total}"
        return output


p1 = Product(12345, "Hat", 10)
p2 = Product(24680, "Glove", 20)
p3 = Product(36912, "Boots", 30)

shopping = Purchase()
shopping.add_to_cart(PurchaseItem(p1, 1))
shopping.add_to_cart(PurchaseItem(p2, 2))
shopping.add_to_cart(PurchaseItem(p3, 3))
print(shopping.checkout("cash"))