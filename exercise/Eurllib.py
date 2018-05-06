#!/usr/bin/env python  
# -*- coding: utf-8  -*-
#time:'2018/5/5 下午 1:15'
#author:'jiayiming'

'''
测试urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, content=None)
'''
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
res =  response.read().decode('utf-8') #将二进制数据编码成utf-8
#print(res)

#timeout
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')


