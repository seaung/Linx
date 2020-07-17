import urllib.request
import re


class WebCrawler(object):
    def __init__(self):
        self.links = []
        self.status = {}
        self.port = None
        self.url = None

