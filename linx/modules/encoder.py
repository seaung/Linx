import base64
import hashlib
import html
import urllib.parse
from typing import Optional

class Encoder:
    """编码器类，提供常见的编码解码功能"""
    
    @staticmethod
    def encode(text: str, method: str) -> Optional[str]:
        """编码函数
        支持base64、url、html、md5、sha1、sha256、sha512编码
        """
        try:
            if method == 'base64':
                return base64.b64encode(text.encode()).decode()
            elif method == 'url':
                return urllib.parse.quote(text)
            elif method == 'html':
                return html.escape(text)
            elif method == 'md5':
                return hashlib.md5(text.encode()).hexdigest()
            elif method == 'sha1':
                return hashlib.sha1(text.encode()).hexdigest()
            elif method == 'sha256':
                return hashlib.sha256(text.encode()).hexdigest()
            elif method == 'sha512':
                return hashlib.sha512(text.encode()).hexdigest()
            else:
                return None
        except Exception:
            return None
    
    @staticmethod
    def decode(text: str, method: str) -> Optional[str]:
        """解码函数
        支持base64、url、html的解码
        注意：哈希编码是不可逆的，所以不提供解码
        """
        try:
            if method == 'base64':
                return base64.b64decode(text.encode()).decode()
            elif method == 'url':
                return urllib.parse.unquote(text)
            elif method == 'html':
                return html.unescape(text)
            else:
                return None
        except Exception:
            return None