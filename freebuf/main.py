__author__ = 'Administrator'
import os,sys,time

from extra.regedit import *
from extra.urlopen import *
from extra.proxydb import *

class Factory():
    def updateProxy(self):
        self.disableProxy()
        self.start_spider()
        self.filter_proxy()

    def updateUrl(self):
        self.disableProxy()
        os.system("scrapy crawl freebuf")

    def funcFb(self, num=10):
        pdb = ProxyDb(r'data/proxy.db')
        proxylist = pdb.selectProxy('good_proxy')
        count = 0
        while count<num:
            for proxy in proxylist:
                SetProxyProcess(proxy)
                if self.visitFb()==False:
                    proxylist.remove(proxy)
                #os.system("pause")
            count += 1

    def dropTable(self):
        pdb = ProxyDb(r'data/proxy.db')
        pdb.dropTable('fburl')

    def disableProxy(self):
        reg = ProxyReg()
        reg.setProxyDisable()

    def visitFb(self):
        pdb = ProxyDb(r'data/proxy.db')
        urllist = pdb.selectProxy('fburl')
        urlopen = MulitUrlopen()
        count = 5
        tout = 4
        for url in urllist:
            if urlopen.visit(url, tout):
                count -= 1
            else:
                count += 1
                tout += 1
            if count>10:
                return False
        return True

    def start_spider(self):
        os.system("scrapy crawl daili")

    def filter_proxy(self):
        pdb = ProxyDb(r'data/proxy.db')
        ip_list = pdb.selectProxy('proxy', 0, 200)
        for ip in ip_list:
            SetProxyProcess(ip)
            if pingTest():
                print "great ip:", ip
                pdb.addProxy('good_proxy', ip)
            else:
                pdb.delProxy('proxy',ip)
                pdb.delProxy('good_proxy', ip)

if __name__ == '__main__':
    fac = Factory()
    usage = "usage:\n --drop :drop url list\n --upurl :update url\n --upproxy :update proxy\n --visit :visit url\n --help :usage"
    select = sys.argv[1]
    #select = raw_input("input:")
    if select=='--drop':
        fac.dropTable()
    elif select=='--upurl':
        fac.updateUrl()
    elif select=='--upproxy':
        fac.updateProxy()
    elif select=='--visit':
        fac.funcFb()
    elif select=='--help':
        print usage
    else:
        print usage

    fac.disableProxy()

