import unittest

import vector

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.v1 = vector.Vector2D(0, 0)
        self.v2 = vector.Vector2D(-1, 1)
        self.v3 = vector.Vector2D(2.5, -2.5)

    def test_equality(self):
        """ Tests the equality operator.
        """
        self.assertNotEqual(self.v1, self.v2)
        expected_result = vector.Vector2D(-1, 1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self):
        """ Tests the addition operator.
        """
        result = self.v1 + self.v2
        expected_result = vector.Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        """ Tests the subtraction operator.
        """
        result = self.v2 - self.v3
        expected_result = vector.Vector2D(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        """ Tests the multiplication operator.
        """
        result1 = self.v1 * 5
        expected_result1 = vector.Vector2D(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.v1 * self.v2
        expected_result2 = 1.0
        self.assertEqual(result2, expected_result2)
        
if __name__ == '__main__':
    unittest.main()
