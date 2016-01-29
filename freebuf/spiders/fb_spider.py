__author__ = 'Administrator'

import scrapy
from freebuf.extra.proxydb import *

class FbSpder(scrapy.Spider):
    name = "freebuf"
    allowed_doamins = ["freebuf.com"]
    start_urls = [
        "http://www.freebuf.com/author/secdarker",
        "http://www.freebuf.com/author/%e4%b8%9c%e4%ba%8c%e9%97%a8%e9%99%88%e5%86%a0%e5%b8%8c",
        "http://www.freebuf.com/author/%e8%80%81%e7%8e%8b%e9%9a%94%e5%a3%81%e7%9a%84%e7%99%bd%e5%b8%bd%e5%ad%90",
    ]

    def parse(self, response):
        url_list = []
        for sel in response.xpath('//div[@class="tit"]/a/@href'):
            url = sel.extract()
            url_list.append(url)

        pdb = ProxyDb(r'data/proxy.db')
        for url in url_list:
            pdb.addProxy('fburl', url)