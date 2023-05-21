products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


prices = []
for product, price in products:
    prices.append(price)

product_prices = map(lambda product: product[1], products)
price_only = []
for price in product_prices:
    price_only.append(price)
    print(price)

print(prices)
