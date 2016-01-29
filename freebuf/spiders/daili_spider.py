__author__ = 'Administrator'

import scrapy
from freebuf.extra.proxydb import *

class DailiSpider(scrapy.Spider):
    name = "daili"
    allowed_doamins = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/nt/",
        "http://www.xicidaili.com/nn/",
    ]

    def parse(self, response):
        iplist = []
        for sel in response.xpath('//table/tr'):
            try:
                tddata = sel.xpath('td/text()')
                ipaddr = tddata[0].extract()
                port = tddata[1].extract()
                writebuf = ipaddr + ':' + port
                iplist.append(writebuf)
            except:
                print 'get fail'

        db = ProxyDb(r'data/proxy.db')
        for ip in iplist:
            db.addProxy('proxy', ip)