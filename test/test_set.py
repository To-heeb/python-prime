"""Test set
"""
import unittest


class SetTestCase(unittest.TestCase):

    def test_are_all_vowels_in_string(self):
        string = "sequoia"
        result = {char for char in string if char in 'aeiou'}
        self.assertSetEqual(result, {'a', 'e', 'i', 'o', 'u'})

    def test_set_methods(self):
        math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
        biology_students = {"Jane", "John", "Matthew",
                            "Charles", "Charlotte", "Mesut", "James", "Olivet"}
        union = math_students | biology_students
        self.assertSetEqual(union, {'Mesut', 'Charlotte', 'Jane', 'Matthew',
                            'Prashant', 'James', 'Olivet', 'John', 'Charles', 'Aparna', 'Helen'})


if __name__ == '__main__':
    unittest.main()
