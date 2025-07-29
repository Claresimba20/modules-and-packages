import unittest
def add(a,b):
    return a+b
class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(3,4),7)

    def test_add_negative(self):
        self.assertEqual(add(-3,-4),-7)

    #assetin
    def test_result_in_list(self):
        result=add(2,3)
        self.assertIn(result, [4,5,6])

    #assertgreater
    def test_result_greater_than(self):
        result=add(5,2)
        self.assertGreater(result,6)

    #assertTrue
    def test_result_true(self):
        self.assertTrue(add(1,2)==3)


if __name__=="__main__":
    unittest.main()

#add two more test cases+functions
#assertin,assertgreater,asserttrue