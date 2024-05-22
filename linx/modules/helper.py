import base64
import fcntl
import socket
import struct
from typing import Any


def decode(bstr: str) -> str:
    text = input('[*] string to be decoded')
    decode = text.decode('{}'.format(bstr))
    result = '[+] Result: {}'.format(decode)
    return result


def endcode(bstr: str) -> str:
    text = input('[*] string to be decoded')
    decode = text.encode('{}'.format(bstr))
    result = '[+] Result: {}'.format(decode)
    return result


def get_local_ip(interface: str) -> Any:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno, 0x8915, struct.pack('256s', interface[:15]))[20:24])

