import unittest


def add(x):
    return x + 1


class AddTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(1), 2)

if __name__ == '__main__':
    unittest.main()
