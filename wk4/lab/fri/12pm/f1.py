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

Purchase
    attributes
        items: list of PurchaseItems
    action
        accepted_payment_types(): list of payment types
        checkout(payment_type)

PurchaseItem
    attributes
        product: Product
        quantity:
    actions
        tostring: summary PurchaseItem
"""