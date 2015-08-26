import os.path
import tempfile
import unittest
from unittest import mock


class MyError(Exception):
    pass


def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise MyError


class RmTestCase(unittest.TestCase):

    @mock.patch('__main__.os')
    def test_rm(self, mock_os):
        rm('/tmp/tmpfile')
        mock_os.remove.assert_called_with('/tmp/tmpfile')

    @mock.patch.object(os, 'remove', side_effect=FileNotFoundError)
    def test_rm_without_file(self, mock_remove):
        with self.assertRaises(MyError) as context:
            rm('not_exist_file')


if __name__ == '__main__':
    unittest.main()
