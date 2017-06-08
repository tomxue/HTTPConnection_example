#!/usr/bin/python
# -*- coding: UTF-8 -*-

import httplib  

# 参数strict默认为false，表示在无法解析状态行时(statusline)不能被HTTP/1.0或1.1解析时不抛出BadStatusLine异常；
# 可选参数timeout表示即阻塞在多少秒后超时，如果没有给出默认使用全局超时设置
conn=httplib.HTTPConnection('www.baidu.com',80,False,10)
conn.request('GET','')
res = conn.getresponse()
print res.read()
