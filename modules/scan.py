import socket
from threading import Thread
from lib.tools.utils import success, error, info


def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(success(f"Lins > {host}:{port} state open"))
        sock.close()
    except Exception as e:
        print(error(f"Lins > {e}"))
        print(error("Lins > socket error."))


def run_default_scan(host):
    print(info(f"Lins > start scan {host} ..."))
    for port in range(1, 1024):
        t = Thread(target=port_scan, args=(host, port))
        t.start()
        if port % 500 == 0:
            t.join()
