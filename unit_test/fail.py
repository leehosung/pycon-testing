import unittest


def add(x):
    return x + 1


class AddTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1), 2)

    def test_add_fail(self):
        self.assertEqual(add(1), 3)

    def test_wrong_parameter(self):
        add('dummy')

if __name__ == '__main__':
    unittest.main()
