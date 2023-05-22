import unittest
import random


class VariablesAndStringTestcase(unittest.TestCase):
    """Test that variables and strings file

    Args:
        unittest (_type_): _description_
    """

    def test_milage(self):
        """Test milage conversion is correct
        """
        kms = random.randint(0, 10)
        miles = kms/1.60934
        self.assertEqual(miles, kms/1.60934)
        self.assertNotEqual(miles, 1.60934)


if __name__ == '__main__':
    unittest.main()
