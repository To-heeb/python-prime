products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


filtered_list = filter(lambda product: product[1] >= 10, products)

for product in filtered_list:
    print(product)
