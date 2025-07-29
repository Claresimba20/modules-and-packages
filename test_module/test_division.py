import unittest
from operations.division import division

class TestDivision(unittest.TestCase):
    def test_divide_positive(self):
        self.assertEqual(division(6,3),2)
    def test_divide_negative(self):
        self.assertEqual(division(-6,-3),2)

if __name__=="__main__":
    unittest.main()