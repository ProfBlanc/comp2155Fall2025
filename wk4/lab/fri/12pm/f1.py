"""
Create a script that organizes and structures
a checkout/purchase operations

Product
    attributes
        barcode
        name: min 3 chars
        price: 6 mnums
    action
        tostring

Store
    attributes
        name: min 3 chars
        inventory: collection of Products (list[Product])
    actions
        add_product: add product to inventory
        remove_product

PurchaseItem
    attributes
        product:
        quantity:
    actions
        tostring: summary PurchaseItem

Purchase
    attributes
        items: list of PurchaseItems
    action
        add_to_cart(PurchaseItem)
        remove_from_cart(PurchaseItem)
        accepted_payment_types(): list of payment types
        checkout(payment_type)

"""
class Name:
    def __init__(self, name):
        self.name = name
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not type(value) == str and len(value) < 3: ValueError("Invalid Name")
        self.__name = value

class Product(Name):
    def __init__(self, barcode, name, price):
        super().__init__(name)
        self.barcode = barcode
        self.price = price
    @property
    def barcode(self): return self.__barcode
    @barcode.setter
    def barcode(self, value):
        if not type(value) == int and len(str(value)) < 5: raise ValueError("Invalid barcode")
        self.__barcode = value
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) and value < 0: raise ValueError("Invalid Price")
        self.__price = value
    def __str__(self): return f"Product Barcode = {self.barcode}, " \
                              f"Product Name = {self.name}, Product Price = ${self.price: .2f}"

class Store(Name):
    def __init__(self, name):
        super().__init__(name)
        self.__inventory = list()
    def add_product(self, p):
        if not type(p) == Product: raise TypeError("Invalid Argument. Not a Product")
        self.__inventory.append(p)
    def remove_product(self, p):
        if not type(p) == Product: raise TypeError("Invalid Argument. Not a Product")
        elif p not in self.__inventory: raise ValueError("Product not in inventory")
        self.__inventory.remove(p)
    def display_inventory(self):
        output = ""
        for p in self.__inventory:
            output += str(p) + "\n"
        return output

class PurchseItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Purchase:
    def __init__(self):
        self.__items = list()
        self.__payment_type = self.acceptable_payment_methods()[0]

    @staticmethod
    def acceptable_payment_methods(): return "cash,credit,debit".split(",")

    def add_to_cart(self, purchase_item):
        if not isinstance(purchase_item, PurchseItem): raise TypeError("Not a Purchase Item")
        self.__items.append(purchase_item)
    def checkout(self, payment_type):
        if payment_type not in self.acceptable_payment_methods(): raise ValueError("invalid payment type")

        total = 0
        for item in self.__items:
            total += item.product.price * item.quantity

        return f"Your Grand Total is ${total:.2f}"

p1 = Product(name="Food", barcode=12345, price=10)
p2 = Product(name="Drink", barcode=24680, price=5)
p3 = Product(name="Clothes", barcode=36912, price=30)

purchase = Purchase()
purchase.add_to_cart(PurchseItem(p1, 1))
purchase.add_to_cart(PurchseItem(p2, 2))
purchase.add_to_cart(PurchseItem(p3, 3))

print(purchase.checkout("cash"))