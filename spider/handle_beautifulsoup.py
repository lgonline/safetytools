#!/usr/bin/env python
# encoding: utf-8

"""
@project: safetytools
@author: root
@software: PyCharm
@file: safetytools 
@time: 7/24/17
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('kali.html'))

if __name__ == '__main__':
    #soup = BeautifulSoup(kali,'html',from_encoding='utf-8')
    print 'soup.title : ',soup.title
    print 'soup.title.name : ',soup.title.name
    print 'soup.name : ',soup.name
    pass