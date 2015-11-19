#!/usr/bin/env python
# coding=utf-8
import urllib.request
import json
#参数phone为提交的号码
url = 'http://apis.baidu.com/apistore/mobilenumber/mobilenumber?phone=13705049067'
req=urllib.request.Request(url)
apikey='743748bfd52d489eac8fbe84aad1619d'
req.add_header('apikey',apikey)
response=urllib.request.urlopen(req)
content=response.read()
if content:
    c=json.loads(content.decode('utf8'))
    print(c['retData'])
