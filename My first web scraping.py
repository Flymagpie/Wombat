#!/usr/bin/python
# -*- coding: UTF-8 -*- 


import requests
r = requests.get("http://httpbin.org/get")

print(type(r))
print(r.status_code)
print(r.encoding)
#print(r.text)
print(r.cookies)

