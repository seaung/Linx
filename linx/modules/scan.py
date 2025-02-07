import socket
import threading
from concurrent.futures import ThreadPoolExecutor


class Scanner(object):
    def __init__(self, target: str, port: list = []) -> None:
        if port is None:
            self.ports = [21, 22, 23, 25, 53, 57, 79, 80, 107]
        else:
            self.ports = port

        self.target = target
        self.timeout = 3
        self.open_ports = []
        self.lock = threading.Lock()

    def tcp_scan(self, port: int) -> bool:
        '''TCP端口扫描'''
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = 'unknown'
                with self.lock:
                    self.open_ports.append((port, service))
                return True
            return False
        except:
            return False
        finally:
            sock.close()

    def port_scan(self) -> list:
        '''扫描目标主机开放的端口'''
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.tcp_scan, self.ports)
        return self.open_ports

