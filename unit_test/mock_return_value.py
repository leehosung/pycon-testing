import os.path
import tempfile
import unittest
from unittest import mock


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)


class RmTestCase(unittest.TestCase):

    @mock.patch('__main__.os.path')
    @mock.patch('__main__.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm('/tmp/tmpfile')
        self.assertFalse(mock_os.remove.called)

        mock_path.isfile.return_value = True
        rm('/tmp/tmpfile')
        mock_os.remove.assert_called_with('/tmp/tmpfile')


if __name__ == '__main__':
    unittest.main()
