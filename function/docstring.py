def say_hello():
    """A simple function that returns the string hello"""
    return "hello"


def exponent(num, power=2):
    """exponent(num, power)raises num to specified power. Power defaults to 2."""
    return num ** power


print(say_hello.__doc__)  # "A simple function that returns the string"

print(exponent.__doc__)

print([1, 2, 3].pop.__doc__)
