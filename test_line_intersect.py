import unittest
from line_intersect import  line_intersect

class Test_line_intersect(unittest.TestCase):
    def test_line_interesect(self):
        line = line_intersect([(0, 10), (0, 25)], [(0, 1), (2, 3)])
        expected = (9.0, 10.0)
        self.assertEqual(line, expected)

    def test_same_line(self):
        line_1 = [(-1, -1), (1, 1)]
        line_2 = [(-2, -2), (2, 2)]
        line = line_intersect(line_1, line_2)
        self.assertEqual(line_1, line)

    def test_normal_line(self):
        line_1 = [(0, 2), (2, 0)]
        line_2 = [(-2, -2), (2, 2)]
        line = line_intersect(line_1, line_2)
        expected = (1.0, 1.0)
        self.assertEqual(expected, line)

    def test_unnormal_line(self):
        line1 = [(-3, 0), (0, 3)]
        line2 = [(0, -3), (3, 0)]
        line = line_intersect(line1, line2)
        self.assertIsNone(line)

if __name__ == '__main__':
    unittest.main()