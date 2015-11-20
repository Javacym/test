#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.parse
import json
import base64
#语言处理地址
googleurl='http://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=zh-CN&maxresults=1'
url='http://apis.baidu.com/apistore/vop/baiduvopjson'
apikey='743748bfd52d489eac8fbe84aad1619d'
data={}
data['format'] = "pcm"
data['rate'] = "8000"
data['channel'] = "1"
data['lan'] = "zh"
''' 参数说明
audioBase64 string	是	bodyParam
语音文件base64后的字符串（还有对base64后的字符串进行urlencode编码，很重要）
format string	是	bodyParam
压缩格式。支持：pcm（不压缩）、wav、opus、speex、amr、x-flac   pcm
rate string	是	bodyParam
采样率，支持 8000 或者 16000     8000
channel  string	是	bodyParam
声道数，仅支持单声道，请填写 1    1
lan string	否	bodyParam
系统支持语言种类：中文（zh）、粤语（ct）、英文（en） zh
#1、原始语音的录音格式目前只支持评测 8k/16k 采样率 16bit 位深的单声道语音
'''
# base64模块b64encode

# data['audioBase64']=''
decode_data=urllib.parse.urlencode(data)
# json_data=json.dumps(data)
headers={'Content-Type':'application/x-www-form-urlencoded',
        'apikey':apikey}
req=urllib.request.Request(url,data=bytes(decode_data,encoding='utf8'),headers=headers)
# req=urllib.request.Request(url,data=json_data,headers=headers)
response=urllib.request.urlopen(req)
content=response.read()
_content=str(content,encoding='utf8')
obj=json.loads(_content)
if obj:
    print(obj)
