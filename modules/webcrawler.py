import requests
import re


class WebCrawler(object):
    def __init__(self, domain, key, depth=3):
        self.domain = domain
        self.depth = depth
        self.url_links = set([])
        self.key = key

    def extractor(self, url):
        try:
            headers = {"User-Agent": "spider"}
            response = requests.get(url=url, headers=headers, timeout=3)
            response.encoding = response.apparent_encoding
            content = response.text
            links = re.findall(r'(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')', content)
        except:
            return set([])

        url_lists = set([])

        for link in links:
            if self.key in url:
                url_lists.add(link)

        url_lists = set(url_lists)-self.url_links
        self.url_links.update(url_lists)

        return url_lists
    
    def crawler(self):
        url_links = set(self.domain)
        while self.depth >= 1:
            url_links_tmp = set([])
            for link in url_links:
                url_links_tmp.update(self.extractor(link))
            url_links = url_links_tmp
            self.depth = self.depth - 1

