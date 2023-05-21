products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_products(product):
    return product[1]


# products.sort(key=sort_products)
# lmada function/ anonymous function (lambda parameter:expression)
products.sort(key=lambda product: product[1])
print(products)
