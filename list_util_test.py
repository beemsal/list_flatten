import unittest

from list_util import ListUtil


class TestListUtil(unittest.TestCase):

    def test_empty_missing(self):
        lu = ListUtil([])
        self.assertEqual(lu.flatten(), [])

    def test_flat_to_flat(self):
        lu = ListUtil([0, 1, 2])
        self.assertEqual(lu.flatten(), [0, 1, 2])

        lu = ListUtil([0, 5, 9])
        self.assertEqual(lu.flatten(), [0, 5, 9])

    def test_nest_to_flat(self):
        lu = ListUtil([[1, 2, [3]], 4])
        self.assertEqual(lu.flatten(), [1, 2, 3, 4])

        lu = ListUtil([0, 1, [0, 1, 2]])
        self.assertEqual(lu.flatten(), [0, 1, 0, 1, 2])

        lu = ListUtil([[3, [8, [4, 2, 1], 7], 6], 0, 1, [0, 1, 2]])
        self.assertEqual(lu.flatten(), [3, 8, 4, 2, 1, 7, 6, 0, 1, 0, 1, 2])

        lu = ListUtil([[1, 2, 3], [1, 2, 3], [1, 2, [1, 2, [[]]]]])
        self.assertEqual(lu.flatten(), [1, 2, 3, 1, 2, 3, 1, 2, 1, 2])

if __name__ == '__main__':
    unittest.main()