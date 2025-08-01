import unittest
from operations.addition import add

class TestAddition(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2,3),5)
    def test_add_negative(self):
        self.assertEqual(add(-2,-3),-5)

if __name__=="__main__":
    unittest.main()