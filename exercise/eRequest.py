#!/usr/bin/env python  
# -*- coding: utf-8  -*-
#time:'2018/5/5 下午 10:41'
#author:'jiayiming'

'''
构建一个request.Request对象
'''
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print("status: {}".format(response.status))
print("headers: {}".format(response.getheaders()))
print("server: {}".format(response.getheader('Server')))
print(response.read().decode('utf-8'))

#解析url链接

from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result)