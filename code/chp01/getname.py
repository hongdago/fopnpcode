#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:search1.py
DESC:将主机名转换为IP地址
"""

import socket

if __name__ == '__main__':
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
