import unittest
from operations.subtraction import subtraction

class TestSubtraction(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtraction(5,2),3)
    def test_subtract_negative(self):
        self.assertEqual(subtraction(-10,-5),-5)


if __name__=="__main__":
    unittest.main()