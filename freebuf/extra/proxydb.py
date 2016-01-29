__author__ = 'Administrator'
import sqlite3

class ProxyDb():
    def __init__(self, dbfile):
        try:
            self.cx = sqlite3.connect(dbfile)
            self.cu = self.cx.cursor()
        except Exception,ex:
            print Exception,':',ex
        self.dbInit()

    def dbInit(self):
        try:
            create_table = 'CREATE TABLE IF NOT EXISTS proxy (id INTEGER PRIMARY KEY, ipport TEXT UNIQUE)'
            self.cu.execute(create_table)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex
        try:
            create_table_gpc = 'CREATE TABLE IF NOT EXISTS good_proxy (id INTEGER PRIMARY KEY, ipport TEXT UNIQUE)'
            self.cu.execute(create_table_gpc)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex

        try:
            create_table_url = 'CREATE TABLE IF NOT EXISTS fburl (id INTEGER PRIMARY KEY, ipport TEXT UNIQUE)'
            self.cu.execute(create_table_url)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex

    def addProxy(self, tbname, ipdata):
        try:
            insert_data = 'INSERT INTO %s(ipport) VALUES ("%s")'%(tbname, ipdata)
            self.cu.execute(insert_data)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex

    def delProxy(self,tbname, ipdata):
        try:
            del_data = 'DELETE FROM %s WHERE ipport = "%s"'%(tbname, ipdata)
            self.cu.execute(del_data)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex

    def selectProxy(self, tbname, m=0, n=100):
        ip_list = []
        try:
            selcet_data = 'SELECT ipport FROM %s LIMIT %d,%d'%(tbname,m,n)
            self.cu.execute(selcet_data)
            res = self.cu.fetchall()
            for item in res:
                ip_list.append(item[0])
        except Exception,ex:
            print Exception,':',ex
        finally:
            return ip_list

    def dropTable(self,tbname):
        try:
            drop_tb = 'DROP TABLE %s'%tbname
            print drop_tb
            self.cu.execute(drop_tb)
            self.cx.commit()
        except Exception,ex:
            print Exception,':',ex

    def __del__(self):
        self.cu.close()
        self.cx.close()

'''
if __name__ == '__main__':
    pdb = ProxyDb(r'../data/proxy.db')
    print pdb.selectProxy('proxy')'''