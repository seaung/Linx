import re
from urllib import request

file_ext = []

class CrawlerSpider(object):
    def __init__(self) -> None:
        self.links = []

    def get_content(self, target: str) -> str:
        '''获取网页内容'''
        self.url = target
        try:
            host = self.url.split('://')[1].split(':')[0]
        except:
            host = self.url.split('://')[1]
        host = self.url.split('://')[0] + '://' + host
        response = request.urlopen(self.url, timeout=3)
        if response.status == 200:
            return response.read().decode('utf-8')
        return ""

    def run(self, target: str):
        pass

