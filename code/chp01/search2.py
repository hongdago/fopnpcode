#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:search2.py
DESC:从谷歌地理编码API获取一个JSON文档, 通过requests库
"""

import requests

def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocoder/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])


if __name__ == "__main__":
    geocode('207 N. Defiance St, Archbold, OH')
