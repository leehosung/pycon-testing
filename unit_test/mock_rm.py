import os.path
import tempfile
import unittest
from unittest import mock


def rm(filename):
    os.remove(filename)


class RmTestCase(unittest.TestCase):

    @mock.patch('__main__.os')
    def test_rm(self, mock_os):
        rm('/tmp/tmpfile')
        mock_os.remove.assert_called_with('/tmp/tmpfile')


if __name__ == '__main__':
    unittest.main()
