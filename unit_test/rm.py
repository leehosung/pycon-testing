import os.path
import tempfile
import unittest


def rm(filename):
    os.remove(filename)


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), 'temp-testfile')

    def setUp(self):
        with open(self.tmpfilepath, 'w') as f:
            f.write('Delete me!')

    def tearDown(self):
        if os.path.isfile(self.tmpfilepath):
            os.remove(self.tmpfilepath)

    def test_rm(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), 'Failed to remove the file')


if __name__ == '__main__':
    unittest.main()
