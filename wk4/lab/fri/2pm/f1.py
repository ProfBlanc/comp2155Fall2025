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
        if isinstance(value, str) and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Invalid Name")

class Product(Name):
    def __init__(self, barcode, name, price):
        super().__init__(name)
        self.barcode = barcode
        self.price = price
    @property
    def barcode(self): return self.__barcode
    @barcode.setter
    def barcode(self, value):
        if type(value) != int and len(str(value)) < 5: raise ValueError("Invalid Barcode")
        else: self.__barcode = value
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) and value < 0: raise ValueError("Invalid Price")
        else: self.__price = value
    def __str__(self): return f"Barcode={self.barcode},Name={self.name},Price=${self.price:.2f}"


class Store(Name):
    def __init__(self, name):
        super().__init__(name)
        self.__inventory = list()
    def add_product(self, p):
        if not type(p) == Product: raise TypeError("Not a Product")
        self.__inventory.append(p)
    def remove_product(self, p):
        if not type(p) == Product and p not in self.__inventory: ValueError("Not a Product or Product not found")
        self.__inventory.remove(p)

class PurchaseItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    def __str__(self): return f"{str(self.product)},Qauntity={self.quantity}"

class Purchase:
    def __init__(self):
        self.__items = list()
        self.__payment_method = self.acceptable_payments()[0]
    def add_to_cart(self, purchase_item):
        if not isinstance(purchase_item, PurchaseItem): raise TypeError("NOT a purchase item")
        self.__items.append(purchase_item)
    @staticmethod
    def acceptable_payments(): return "cash,credit,debit".split(",")
    def checkout(self, payment_method):
        if payment_method not in self.acceptable_payments(): raise ValueError("Invalid Payment Method")
        if len(self.__items) == 0: raise ValueError("No items in cart")
        self.__payment_method = payment_method
        output = ""
        total = 0
        for item in self.__items:
            output += str(item) + "\n"
            total += item.product.price * item.quantity
        output += "Payment Method = " + self.__payment_method + "\n"
        output += f"Grand Total = ${total: .2f}"
        return output

p1 = Product(barcode=12345, name="Food", price=10)
p2 = Product(barcode=24680, name="Drink", price=5)
p3 = Product(barcode=36912, name="Gas", price=30)

purchase = Purchase()
purchase.add_to_cart(PurchaseItem(p1, 1))
purchase.add_to_cart(PurchaseItem(p2, 2))
purchase.add_to_cart(PurchaseItem(p3, 3))
print(purchase.checkout("credit"))
