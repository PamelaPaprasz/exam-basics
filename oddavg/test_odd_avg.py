import unittest
import odd_avg 

class TestOddAvg(unittest.TestCase):
    def setUp(self):
        pass

    def test_only_odds(self):
        self.assertEqual(odd_avg.odd_average([5, 3, 5, 3]), 4)
    
    def test_one_even(self):
        self.assertEqual(odd_avg.odd_average([6]), 0)
    
    def test_result_float(self):
        self.assertEqual(odd_avg.odd_average([1, 4, 7, 2, 5, 3, 5, 3, 1]), 3.5714285714285716)
    

if __name__ == '__main__':
    unittest.main()
    