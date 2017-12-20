#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:search1.py
DESC:通过第三方库pygeocoder，获取经度和维度
"""

from pygeocoder import Geocoder

if __name__ == "__main__":
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
