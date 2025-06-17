# test_calculator_unittest.py
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 7), 3)
    
    def test_multiply(self):
        self.assertEqual(multiply(5, 6), 30)
    
    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()