#!/usr/bin/env python
# coding:utf-8

import chardet
import codecs

def readfile(filename):
    with open(filename) as f:
        data = f.readlines()
    return data
f1 = r'e:\a.txt'
f2 = r'e:\b.txt'

a1 = readfile(f1)
a2 = readfile(f2)
#
# for i in a1:
#     print i,
#
# print '\n-----------'
# for i in a2:
#     print i.decode('gbk').encode('utf-8'),

# for i in a1:
#     print chardet.detect(i)

# f3 = codecs.open(f2,mode='rb',encoding='gbk').readlines()
# for i in f3:
#     print i

import os
import base64

f_path = r'd:\python340.chm'

with open(f_path) as f:
    data = base64.b64decode(f.read())

for i in data:
    print i
