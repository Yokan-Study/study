# Unit Test

import unittest
import lshJoin
import lshSum10

class lshTests(unittest.TestCase):
    def test_join(self):
        str = ['I', 'love', 'python !']
        result = lshJoin.join(str)
        self.assertEqual(result, 'I love python !')

    def test_sum10(self):
        one_to_ten = range(1,11)
        result = lshSum10.sum10(one_to_ten)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()