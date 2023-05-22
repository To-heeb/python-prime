import unittest


def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    return f"Printed {text} in {color}"


class FunctionTestCase(unittest.TestCase):

    def test_colorize_exception(self):
        self.assertRaises((TypeError, ValueError),
                          colorize, "Toheeb", "pink")

    def test_colorize_with_exception(self):

        with self.assertRaises((TypeError, ValueError)):
            colorize("Toheeb", "pink")

    def test_colorize(self):
        text = "Toheeb"
        color = "cyan"
        self.assertEqual(colorize(text=text, color=color),
                         f"Printed {text} in {color}")
