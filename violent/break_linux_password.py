#!/usr/bin/env python
# encoding: utf-8

"""
@author: root
@software: PyCharm
@file: break_linux_password.py
@time: 7/20/17 12:11 PM
"""

import crypt

passwds = ['123456','000000','1qaz2wsx','1q2w3e4r']

def generate_password_using_crypt(passwds):
    for passwd in passwds:
        crypt_password = crypt.crypt(passwd,'HX')
        print crypt_password


if __name__ == '__main__':
    generate_password_using_crypt(passwds)
    pass