__author__ = 'Administrator'

import urllib2

class MulitUrlopen():
    def visit(self, url, tout):
        flag = False
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            opener.open(url, timeout=tout)
            flag = True
            print url
        except Exception,ex:
            print Exception,':',ex,url
        finally:
            return flag


def pingTest():
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        opener.open("http://www.126.com", timeout=3)
        return True
    except Exception,ex:
        print Exception,':',ex
    return False
