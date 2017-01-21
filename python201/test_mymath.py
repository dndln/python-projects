import mymath
import unittest

class TestAdd(unittest.TestCase): # subclass TestCase
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct total
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test that the addition of two strings returns the correct total
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

class TestSubtract(unittest.TestCase):
    """
    Test the subtract functino from the mymath library
    """

    def test_subtract_integers(self):
        """
        Test that subtracting integers returns the correct result
        """
        result = mymath.subtract(10, 8)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

# run with python test_mymath.py -v
