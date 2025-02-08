import unittest
from unittest.mock import patch, MagicMock
from linx.modules.wifi import WiFiManager

class TestWiFiManager(unittest.TestCase):
    def setUp(self):
        self.interface = 'en0'
        self.wifi = WiFiManager(self.interface)

    @patch('subprocess.Popen')
    def test_scan_networks(self, mock_popen):
        # 模拟扫描结果
        mock_process = MagicMock()
        mock_process.communicate.return_value = (
            b'SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)\n' +
            b'MyWiFi 00:11:22:33:44:55 -50 11     Y  US WPA2(PSK/AES/AES)\n',
            b''
        )
        mock_popen.return_value = mock_process

        networks = self.wifi.scan_networks()
        self.assertTrue(len(networks) > 0)
        self.assertEqual(networks[0]['ssid'], 'MyWiFi')
        self.assertEqual(networks[0]['bssid'], '00:11:22:33:44:55')
        self.assertEqual(networks[0]['rssi'], '-50')
        self.assertEqual(networks[0]['channel'], '11')
        self.assertEqual(networks[0]['security'], 'WPA2(PSK/AES/AES)')

    @patch('subprocess.Popen')
    def test_crack_network(self, mock_popen):
        # 模拟破解过程
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'', b'')
        mock_popen.return_value = mock_process

        with patch('builtins.open', unittest.mock.mock_open(read_data='password123\nwrongpass\n')):
            password = self.wifi.crack_network('TestWiFi', 'test_wordlist.txt')
            self.assertIsNotNone(password)
            self.assertEqual(password, 'password123')

    @patch('subprocess.Popen')
    def test_disconnect(self, mock_popen):
        # 模拟断开连接
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'', b'')
        mock_popen.return_value = mock_process

        result = self.wifi.disconnect()
        self.assertTrue(result)

    def test_get_current_network(self):
        # 测试获取当前网络
        self.wifi.current_network = 'TestWiFi'
        self.assertEqual(self.wifi.get_current_network(), 'TestWiFi')

    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('builtins.open', unittest.mock.mock_open())
    def test_save_network_config(self, mock_makedirs, mock_exists):
        # 测试保存网络配置
        mock_exists.return_value = False
        result = self.wifi.save_network_config('TestWiFi', 'password123')
        self.assertTrue(result)
        mock_makedirs.assert_called_once()

if __name__ == '__main__':
    unittest.main()