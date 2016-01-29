__author__ = 'Administrator'
import _winreg
import ctypes
import time
import multiprocessing

class SetProxyProcess():
    def __init__(self, ip):
        self.ip = ip
        self.runProcess()

    def setProxy(self, ip):
        srg = ProxyReg()
        srg.setProxyServer(ip)
        srg.setProxyEnable()

    def runProcess(self):
        p = multiprocessing.Process(target=self.setProxy, args=(self.ip,))
        p.start()
        time.sleep(0.5)
        print 'set Proxy finish......'

class ProxyReg():
    def __init__(self):
       self.key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0 ,_winreg.KEY_ALL_ACCESS)

    #set Reg ProxyServer
    def setProxyServer(self, serverip):
        try:
            _winreg.SetValueEx(self.key, "ProxyServer", 0, _winreg.REG_SZ, serverip)
            print "set ProxyServer:value=%s"%serverip
        except WindowsError:
            print "set proxy register fail", WindowsError

    #set Reg ProxyEnable
    def setProxyEnable(self):
        try:
            _winreg.SetValueEx(self.key, "ProxyEnable", 0, _winreg.REG_DWORD, 1)
            self.internet_set_option()
            print "ProxyEnable"
        except Exception,ex:
            print Exception,":",ex

    def setProxyDisable(self):
        try:
            _winreg.SetValueEx(self.key, "ProxyEnable", 0, _winreg.REG_DWORD, 0)
            self.internet_set_option()
            print "Proxy Disable"
        except Exception,ex:
            print Exception,":",ex

    def internet_set_option(self):
        ctypes.windll.Wininet.InternetSetOptionW(0, 37, 0, 0)
        ctypes.windll.Wininet.InternetSetOptionW(0, 39, 0, 0)

    def __del__(self):
        try:
            _winreg.CloseKey(self.key)
        except:
            pass

