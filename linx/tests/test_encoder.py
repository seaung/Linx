import unittest
from linx.modules.encoder import Encoder

class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()
        self.test_text = "Hello, World!"

    def test_base64_encode_decode(self):
        # 测试base64编码解码
        encoded = self.encoder.encode(self.test_text, 'base64')
        self.assertIsNotNone(encoded)
        decoded = self.encoder.decode(encoded, 'base64')
        self.assertEqual(decoded, self.test_text)

    def test_url_encode_decode(self):
        # 测试URL编码解码
        test_url = "https://example.com/?q=测试"
        encoded = self.encoder.encode(test_url, 'url')
        self.assertIsNotNone(encoded)
        decoded = self.encoder.decode(encoded, 'url')
        self.assertEqual(decoded, test_url)

    def test_html_encode_decode(self):
        # 测试HTML编码解码
        test_html = "<script>alert('XSS')</script>"
        encoded = self.encoder.encode(test_html, 'html')
        self.assertIsNotNone(encoded)
        decoded = self.encoder.decode(encoded, 'html')
        self.assertEqual(decoded, test_html)

    def test_hash_encoding(self):
        # 测试哈希编码
        hash_methods = ['md5', 'sha1', 'sha256', 'sha512']
        for method in hash_methods:
            encoded = self.encoder.encode(self.test_text, method)
            self.assertIsNotNone(encoded)
            self.assertTrue(len(encoded) > 0)

    def test_invalid_method(self):
        # 测试无效的编码方法
        result = self.encoder.encode(self.test_text, 'invalid_method')
        self.assertIsNone(result)
        result = self.encoder.decode(self.test_text, 'invalid_method')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()