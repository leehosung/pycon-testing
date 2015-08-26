# from https://github.com/pythonforfacebook/facebook-sdk
import facebook
import unittest
from unittest import mock


class SimpleFacebook(object):

    def __init__(self, oauth_token):
        self.graph = facebook.GraphAPI(oauth_token)

    def post_message(self, message):
        self.graph.put_object('me', 'feed', message=message)


class SimpleFacebookTestCase(unittest.TestCase):

    @mock.patch.object(facebook.GraphAPI, 'put_object', autospect=True)
    def test_post_message(self, mock_put_object):
        sf = SimpleFacebook('fake oauth token')
        sf.post_message('Hello World!')

        mock_put_object.assert_called_with('me', 'feed', message='Hello World!')


if __name__ == '__main__':
    unittest.main()
