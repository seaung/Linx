import unittest
from unittest.mock import patch, MagicMock
from linx.modules.rpc import RPCServer, RPCClient

class TestRPC(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 8888

    @patch('socket.socket')
    def test_server_start(self, mock_socket):
        # 测试服务器启动
        mock_server = MagicMock()
        mock_socket.return_value = mock_server

        server = RPCServer(self.host, self.port)
        server.start()

        mock_socket.assert_called_once()
        mock_server.bind.assert_called_once_with((self.host, self.port))
        mock_server.listen.assert_called_once()

    @patch('socket.socket')
    def test_client_connect(self, mock_socket):
        # 测试客户端连接
        mock_client = MagicMock()
        mock_socket.return_value = mock_client

        client = RPCClient(self.host, self.port)
        client.connect()

        mock_socket.assert_called_once()
        mock_client.connect.assert_called_once_with((self.host, self.port))

    @patch('socket.socket')
    def test_execute_command(self, mock_socket):
        # 测试命令执行
        mock_client = MagicMock()
        mock_socket.return_value = mock_client
        mock_client.recv.return_value = b'Command output'

        client = RPCClient(self.host, self.port)
        client.connect()
        result = client.execute_command('ls -l')

        self.assertEqual(result, 'Command output')
        mock_client.send.assert_called_once_with(b'ls -l')

    @patch('socket.socket')
    @patch('builtins.open', unittest.mock.mock_open(read_data=b'test data'))
    def test_file_transfer(self, mock_socket):
        # 测试文件传输
        mock_client = MagicMock()
        mock_socket.return_value = mock_client
        mock_client.recv.return_value = b'OK'

        client = RPCClient(self.host, self.port)
        client.connect()

        # 测试文件上传
        result = client.upload_file('local.txt', 'remote.txt')
        self.assertTrue(result)

        # 测试文件下载
        result = client.download_file('remote.txt', 'local.txt')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()