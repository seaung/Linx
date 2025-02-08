import unittest
from unittest.mock import patch, MagicMock
from linx.modules.scan import Scanner

class TestScanner(unittest.TestCase):
    def setUp(self):
        self.target = 'example.com'
        self.scanner = Scanner(self.target)

    @patch('socket.socket')
    def test_port_scan(self, mock_socket):
        # 模拟端口扫描
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock
        mock_sock.connect_ex.side_effect = [0, 1, 0]  # 模拟端口80开放，81关闭，443开放

        open_ports = self.scanner.port_scan()
        self.assertEqual(len(open_ports), 2)
        self.assertEqual(open_ports[0][0], 80)
        self.assertEqual(open_ports[1][0], 443)

    def test_get_service_name(self):
        # 测试服务名称识别
        service = self.scanner.get_service_name(80)
        self.assertEqual(service, 'http')
        service = self.scanner.get_service_name(443)
        self.assertEqual(service, 'https')
        service = self.scanner.get_service_name(22)
        self.assertEqual(service, 'ssh')

    @patch('socket.gethostbyname')
    def test_resolve_domain(self, mock_gethostbyname):
        # 测试域名解析
        mock_gethostbyname.return_value = '93.184.216.34'
        ip = self.scanner.resolve_domain()
        self.assertEqual(ip, '93.184.216.34')
        mock_gethostbyname.assert_called_once_with(self.target)

    def test_invalid_target(self):
        # 测试无效目标
        scanner = Scanner('')
        with self.assertRaises(ValueError):
            scanner.port_scan()

if __name__ == '__main__':
    unittest.main()