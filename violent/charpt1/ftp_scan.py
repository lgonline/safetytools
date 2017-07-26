#!/usr/bin/env python
# encoding: utf-8

"""
@author: root
@software: PyCharm
@file: ftp_scan.py
@time: 7/20/17 12:03 PM
"""

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)

        return banner
    except:
        print 'No ftp server in here!'

def main():
    ip1 = '192.168.10.143'
    port = 21

    banner1 = retBanner(ip1,port)

    if banner1:
        print '[+]'+ip1+':'+banner1

if __name__ == '__main__':
    main()
    pass