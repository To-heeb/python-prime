# Class: blueprint for creating new objects
# Object: instance of a class
# self: this is a reference to the current object
# objects in python are dynamic like in javascript
# class attributes are shared accross all instance of the class,
#   once change by one object it affects all other objects.
# instance attributes should be used over class attributes
# instance methods and class methods
# class methods can be called without instantiation of class,
#  if the class requires a defualt value a class method with desualt value can be created and that will be
#  called to give us an instance of the class with defualt value(think about it like a Factory menthod)
# magic methods are called automatically by python interpreter


class Point:
    """Point class for axis coordinates"""

    default_color = "black"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        """
        Returns the zero value of the point class: which makes this a class method that
        instantiates the class with default values
            """
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        """draw this point"""
        print(f"Point ({self.x}, {self.y}))")


point = Point(3, 5)
print(point)
print(str(point))
point.draw()
point.z = 10
print(point.z)
print(point.default_color)
print(Point.default_color)
print(Point.zero().draw())
# print(type(point))
# print(isinstance(point, Point))
