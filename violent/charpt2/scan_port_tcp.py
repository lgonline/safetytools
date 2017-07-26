#!/usr/bin/env python  
# encoding: utf-8   

""" 
@author: root
@software: PyCharm 
@file: scan_port_tcp.py 
@time: 7/25/17 10:53 PM 
"""

import optparse
import socket
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        sockets = socket(AF_INET,SOCK_STREAM)
        sockets.connect((tgtHost,tgtPort))
        sockets.send('ViolentPython\r\n')
        results = sockets.recv(100)
        screenLock.acquire()
        print ' [+] %d/tcp is opened' % tgtPort
        print ' [+] '+str(results)
    except:
        screenLock.acquire()
        print ' [-] %d tcp is closed' % tgtPort
    finally:
        pass
    screenLock.release()
    sockets.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except Exception as e:
        print ' [-] Cannot resolve "%s": Unknown host' % tgtHost
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        #print 'tgtname is : ',tgtName
        print '\n [+] Scan results for : ' +tgtName[0]
    except Exception as e:
        print '\n [+] Scan results for : ' +tgtIP

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

class main():
    parsers = optparse.OptionParser("usage %prog "+"-H <target host> -p <target port>")
    parsers.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parsers.add_option('-p',dest='tgtPort',type='string',help='specify target port[s] separated by comma')

    (options,args) = parsers.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print parsers.usage
        #print ' [-] You must specify a target host and port[s].'
        exit(0)

    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()