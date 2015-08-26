import os
import unittest
from unittest import mock


class RemovalService():

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)


class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch('__main__.os.path')
    @mock.patch('__main__.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        mock_path.isfile.return_value = False
        reference.rm('/tmp/tmpfile')
        self.assertFalse(mock_os.remove.called)

        mock_path.isfile.return_value = True
        reference.rm('/tmp/tmpfile')
        mock_os.remove.assert_called_with('/tmp/tmpfile')


class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(removal_service)

        reference.upload_complete('/tmp/tmpfile')
        removal_service.rm.assert_called_with('/tmp/tmpfile')


if __name__ == '__main__':
    unittest.main()
