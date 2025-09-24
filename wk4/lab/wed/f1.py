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
    p: Product
    quantity
    discount_percentage

Purchase
    list[PurchaseItems]
    checkout(payment_method)

"""


class Name:
    def __init__(self, name):
        self.name = name

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 3:
            raise ValueError("Invalid Name")
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
        if not isinstance(value, int) and len(str(value)) < 5:
            raise ValueError("Invalid Barcode")
        self.__barcode = value

    @property
    def price(self): return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) and value > 0:
            raise ValueError("Invalid Price")
        self.__price = value

    def __str__(self):
        return f"Product Barcode={self.barcode}, Product Name={self.name}, Product Price={self.price}"


class Store(Name):
    def __init__(self, name):
        super().__init__(name)
        self.__inventory = list()

    # add a product to the store inventory
    def add_product(self):
        pass


class PurchaseItem:
    def __init__(self, product: Product, quantity: int)->None:
        self.product = product
        self.quantity = quantity

    @property
    def product(self): return self.__product
    @product.setter
    def product(self, value):
        if not isinstance(value, Product): raise TypeError("Invalid Product")
        self.__product = value

    @property
    def quantity(self): return self.__quantity
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) and value < 1: raise ValueError("Invalid Quantity")
        self.__quantity = value
    def __str__(self):
        return f"{str(self.product)}, Quantity={self.quantity}"


class Purchase:
    def __init__(self):
        self.__items = list()
        self.__payment_type = self.payment_types()[0]

    @staticmethod
    def payment_types(): return "cash,debit,credit".split(",")
    def add_to_cart(self, item):
        if not isinstance(item, PurchaseItem): raise TypeError("Invalid data type")
        self.__items.append(item)
    def remove_from_cart(self, item):
        if item not in self.__items: raise ValueError("Item not found")
        self.__items.remove(item)
    def checkout(self, payment_type):
        if len(self.__items) == 0: raise ValueError("No items in your cart")
        if payment_type.lower() not in self.payment_types(): raise ValueError("Invalid payment type")
        self.__payment_type = payment_type
        total = 0
        output = ""
        for item in self.__items:
            total += item.product.price * item.quantity  # apply discount
            output += str(item.product) + "\n"
        output += "Grand Total = $" + str(round(total, 2))
        return output


p1 = Product(12345, "Coffee", 5)
p2 = Product(24681, "Pastry", 3)
p3 = Product(36912, "Mug", 20)

order = Purchase()
order.add_to_cart(PurchaseItem(p1, 1))
order.add_to_cart(PurchaseItem(p2, 2))
order.add_to_cart(PurchaseItem(p3, 3))
feedback = order.checkout("credit")
print(feedback)
