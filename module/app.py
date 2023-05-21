from ecommerce.shopping.sales import calc_shipping, calc_tax
import ecommerce.shopping.sales as sales
# from ecommerce import sales
import sys

print(sys.path)
print(dir(sales))
print(sales.__name__)
print(sales.__file__)
print(sales.__package__)
sales.calc_shipping()
sales.calc_tax()

calc_shipping()
calc_tax()
