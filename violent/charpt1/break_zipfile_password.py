#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: root
@software: PyCharm 
@file: break_zipfile_password.py 
@time: 7/25/17 10:09 PM

A programe for uzip file password.
"""

import zipfile


#A simple function to meet this requierements
def func_break_zipfile_password():
    myzipfile = zipfile.ZipFile('test.zip')

    password_dict = open('zipfile_password_dict.txt')

    #action:password_dict.readlines()
    for line in password_dict.readlines():
        #print line
        zip_password = line.strip('\n')
        try:
            myzipfile.extractall(pwd=zip_password)
            print ' [+] The password '+zip_password+' is correct.\n'
        except Exception as e:
            print e,'The password '+zip_password+' is bad.'
    pass


#An other function to meet this requirements
def extract_zifile(zipfile,zip_password):
    try:
        zipfile.extractall(pwd=zip_password)
        return zip_password
    except Exception as e:
        #print e
        pass

class Main():
    zipfiles = zipfile.ZipFile('test.zip')
    password_dict = open('zipfile_password_dict.txt')

    for line in password_dict.readlines():
        zip_password = line.strip('\n')
        guess = extract_zifile(zipfiles,zip_password)

        if guess:
            print ' [+] The password '+zip_password+' is correct.\n'
        else:
            print 'The password ' + zip_password + ' is bad.'

    def __init__(self):
        pass






if __name__ == "__main__":
    #call the simple function
    #func_break_zipfile_password()

    #call an other function
    Main()
    pass  