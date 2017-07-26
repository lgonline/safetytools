#!/usr/bin/env python  
# encoding: utf-8   

""" 
@author: root
@software: PyCharm 
@file: nmap_scan.py
@time: 7/26/17 2:01 AM 
"""

import nmap
import optparse

def nampScan(dest_host,dest_port):
    nmScan = nmap.PortScanner()
    nmScan.scan(dest_host,dest_port)
    state = nmScan[dest_host]['tcp'][int(dest_port)]['state']
    print " [*] "+dest_host+" tcp/ "+dest_port+" "+state

class main():
    parsers = optparse.OptionParser('useage %prog'+ '-H <target host> -p <target port>')
    parsers.add_option('-H',dest='dest_host',type='string',help='specify target host')
    parsers.add_option('-p',dest='dest_port',type='string',help='specify target port[s] separated by comma')
    # persers.add_option('-p',dest='dest_port',type='string',help='specify target port[s] separated by comma')

    (options,args) = parsers.parse_args()
    desthost = options.dest_host
    destports = str(options.dest_port).split(',')

    if (desthost == None) | (destports == None):
        print parsers.usage
        exit(0)

    for destports in destports:
        nampScan(desthost,destports)

if __name__ == "__main__":
    main()
    pass  