import unittest

class NumberTest(unittest.TestCase):

    def test_even(self):
        for i in range(0, 6):
            self.assertEqual(i % 2, 0)

    def test_even_with_subtest(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

unittest.main()
