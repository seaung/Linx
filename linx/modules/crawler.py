import re
from urllib import request
from urllib.parse import urljoin, urlparse

file_ext = ['.jpg', '.jpeg', '.png', '.gif', '.css', '.js', '.ico', '.svg']

class CrawlerSpider(object):
    def __init__(self) -> None:
        self.links = []
        self.crawled = set()

    def get_content(self, target: str) -> str:
        '''获取网页内容'''
        self.url = target
        try:
            host = self.url.split('://')[1].split(':')[0]
        except:
            host = self.url.split('://')[1]
        host = self.url.split('://')[0] + '://' + host
        try:
            response = request.urlopen(self.url, timeout=3)
            if response.status == 200:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f'[!] Error fetching {self.url}: {str(e)}')
        return ""

    def extract_links(self, content: str, base_url: str) -> list:
        '''提取页面中的链接'''
        links = []
        pattern = r'href=[\'"]([^\'"]+)[\'"]'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            url = match.group(1)
            # 规范化URL
            url = urljoin(base_url, url)
            # 过滤非目标域名的链接
            if not self._is_same_domain(url, base_url):
                continue
            # 过滤静态资源文件
            if any(url.lower().endswith(ext) for ext in file_ext):
                continue
            links.append(url)
        return links

    def _is_same_domain(self, url1: str, url2: str) -> bool:
        '''判断两个URL是否属于同一域名'''
        domain1 = urlparse(url1).netloc
        domain2 = urlparse(url2).netloc
        return domain1 == domain2

    def run(self, target: str):
        '''开始爬取网站'''
        if not target:
            return
        
        # 初始化爬取队列
        to_crawl = [target]
        
        while to_crawl:
            current_url = to_crawl.pop(0)
            
            # 跳过已爬取的URL
            if current_url in self.crawled:
                continue
                
            print(f'[*] Crawling: {current_url}')
            
            # 获取页面内容
            content = self.get_content(current_url)
            if content:
                # 记录已爬取的URL
                self.crawled.add(current_url)
                self.links.append(current_url)
                
                # 提取新的链接
                new_links = self.extract_links(content, current_url)
                # 添加新的未爬取链接到队列
                for link in new_links:
                    if link not in self.crawled and link not in to_crawl:
                        to_crawl.append(link)
            
        print(f'[+] Crawling finished. Total {len(self.links)} URLs found.')

