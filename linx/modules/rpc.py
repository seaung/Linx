import os
import sys
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RPCServer(object):
    '''RPC服务端'''
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.server = None

    def execute_command(self, command: str) -> str:
        '''执行远程命令'''
        try:
            result = os.popen(command).read()
            return result
        except Exception as e:
            return f"执行失败: {str(e)}"

    def file_upload(self, filename: str, content: bytes) -> bool:
        '''接收文件上传'''
        try:
            with open(filename, 'wb') as f:
                f.write(content)
            return True
        except Exception:
            return False

    def file_download(self, filename: str) -> bytes:
        '''处理文件下载'''
        try:
            with open(filename, 'rb') as f:
                return f.read()
        except Exception:
            return b''

    def start(self) -> None:
        '''启动RPC服务'''
        try:
            self.server = SimpleXMLRPCServer(
                (self.host, self.port),
                requestHandler=SimpleXMLRPCRequestHandler,
                allow_none=True
            )
            self.server.register_function(self.execute_command)
            self.server.register_function(self.file_upload)
            self.server.register_function(self.file_download)
            print(f"[*] RPC服务启动在 {self.host}:{self.port}")
            self.server.serve_forever()
        except Exception as e:
            print(f"[!] RPC服务启动失败: {str(e)}")

class RPCClient(object):
    '''RPC客户端'''
    def __init__(self, host: str, port: int) -> None:
        self.server_url = f"http://{host}:{port}"
        try:
            self.proxy = xmlrpc.client.ServerProxy(self.server_url)
        except Exception as e:
            print(f"[!] 连接服务器失败: {str(e)}")

    def execute_command(self, command: str) -> str:
        '''执行远程命令'''
        try:
            return self.proxy.execute_command(command)
        except Exception as e:
            return f"执行失败: {str(e)}"

    def upload_file(self, local_file: str, remote_file: str) -> bool:
        '''上传文件到远程服务器'''
        try:
            with open(local_file, 'rb') as f:
                content = f.read()
            return self.proxy.file_upload(remote_file, content)
        except Exception:
            return False

    def download_file(self, remote_file: str, local_file: str) -> bool:
        '''从远程服务器下载文件'''
        try:
            content = self.proxy.file_download(remote_file)
            if content:
                with open(local_file, 'wb') as f:
                    f.write(content)
                return True
            return False
        except Exception:
            return False