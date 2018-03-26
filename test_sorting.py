import unittest
from is_sorted import *


class Test_is_sorted(unittest.TestCase):
    def test_false_sorted_list(self):
        """
        test not sorted list
        """
        lst = [0, 1, 4, 2]
        testing = is_sorted(lst)
        self.assertFalse(testing)

    def test_true_sorted_list(self):
        """
        test sorted list
        """
        lst = [0, 1, 2, 3, 4]
        testing = is_sorted(lst)
        self.assertTrue(testing)

    def test_true_sorted_lst_with_negative_values(self):
        """
        test sorted list with negative numbers
        """
        lst = [-2, -3, -4, 5]
        testing = is_sorted(lst)
        self.assertTrue(lst)

    def test_false_sorted_lst_with_negative_values(self):
        """
        test not sorted list with negative numbers
        """
        lst = [-2, -3, 6, 4, 7]
        testing = is_sorted(lst)
        self.assertFalse(testing)

    def test_lst_with_letters(self):
        """
        test sorted list with letters
        """
        lst = ['a', 'b', 1, 2]
        try:
            testing = is_sorted(lst)
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_lst_with_float_numbers(self):
        """
        test list woth float numbers
        """
        lst = [1.1, 1, 2, 3]
        testing = is_sorted(lst)
        self.assertFalse(testing)

    def test_lst_with_same_numbers(self):
        """
        test list with same numbers
        """
        lst = [1, 1, 2, 3, 4]
        testing = is_sorted(lst)
        self.assertTrue(testing)

    def test_lst_with_unusual_parameters(self):
        """
        test some unusual list
        """
        lst = [1, -2+3, 4 - 1, 7]
        testing = is_sorted(lst)
        self.assertTrue(testing)

if __name__ == '__main__':
    unittest.main()
