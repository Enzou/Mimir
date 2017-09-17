import unittest
from pyramid import testing
# import mimir.addons.encoding as encoding
import mimir.addons


class EncodingTests(unittest.TestCase):
    def setUp(self):
        # import mimir.addons.encoding as encoding
        # self.enc = encoding
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_base64_encoding(self):
        b64 = self.enc.Base64
        res = b64.encode("Hello, Mimir")
        self.assertEqual("SGVsbG8sIE1pbWly", res)

        res = b64.encode("Please, I don't want to be decoded :(")
        self.assertEqual("UGxlYXNlLCBJIGRvbid0IHdhbnQgdG8gYmUgZGVjb2RlZCA6KA==")


