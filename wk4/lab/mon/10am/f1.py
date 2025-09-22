"""
Create 2 classes
    Product
        barcode
        name
        description
        price
        toString()
    Store
        name
        inventory: list[Product]
    Purchase
        items: list[Product]
        checkout(payment_type)-> sum of items
"""

class NameValidation:
    def __init__(self, name):
        self.name = name
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 3: raise ValueError("Invalid Name")
        self.__name = value

class Product(NameValidation):
    def __init__(self, barcode, name, description, price):
        super().__init__(name)
        self.barcode = barcode
        self.description = description
        self.price = price

    @property
    def barcode(self):
        return self.__barcode

    @barcode.setter
    def barcode(self, value):
        if not isinstance(value, int) and len(str(value)) < 5: raise ValueError("Invalid Barcode")
        self.__barcode = value

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 3: raise ValueError("Invalid Name")
        self.__name = value
    @property
    def description(self): return self.__description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) and len(value) < 5: raise ValueError("Invalid Description")
        self.__description = value
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) and value <= 0: raise ValueError("Invalid Price")
        self.__price = value

class Store(NameValidation):
    def __init__(self, name, inventory=[]):
        super().__init__(name)
        self.inventory = inventory
    @property
    def inventory(self): return self.__inventory
    @inventory.setter
    def inventory(self, value):
        if isinstance(value, list):
            for v in value:
                if not isinstance(v, Product): raise TypeError("Invalid Inventory Type")
            self.__inventory = value
        else: raise ValueError("Invalid Inventory")

class Purchase:
    def __init__(self):
        self.__items = list()
    def add_to_cart(self, value):
        if not isinstance(value, dict): raise ValueError("Not a product")
        if "product" in value and "quantity" in value and isinstance(value["product"], Product):
            self.__items.append(value)
        else: raise ValueError("Invalid data")
    def _checkout_price(self):
        total = sum([v["product"].price * v["quantity"] for v in self.__items])
        return total
    def _checkout_summary(self):
        output = ""
        for v in self.__items:
            output += f"Product Name={v['product'].name}, Quantity={v['quantity']}, Price={v['product'].price}\n"
        return output

    def checkout(self, payment_type):
        if payment_type.lower() in "visa,debit,cash".split(","):
            summary = self._checkout_summary()
            total = self._checkout_price()
            return f"{summary}{total}"
        else: raise ValueError("Invalid Payment Type")


p1 = Product(name="Hat", description="a fall hat", price=19.99, barcode=12345)
p2 = Product(name="Glove", description="a fall glove", price=29.99, barcode=98765)
p3 = Product(name="Shoe", description="a fall shoe", price=49.99, barcode=24681)

store = Store(name="Corner Store")

store.inventory.append(p1)
store.inventory.append(p2)
store.inventory.append(p3)

purchase = Purchase()
purchase.add_to_cart({"product": p1, "quantity": 1})
purchase.add_to_cart({"product": p2, "quantity": 2})
purchase.add_to_cart({"product": p3, "quantity": 3})

print(purchase.checkout("cash"))
