#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:in_zen2.py
DESC: 对一个或多个客户端连接做出相应， 最终发生超时
"""

import socket, sys, zen_utils


if __name__ == "__main__":
    listener = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('log.txt', 'a', buffering=1)
    listener.settimeout(8.0)
    try:
        zen_utils.accep_connection_foever(listener)
    except socket.timeout:
        print('Waited 8 seconds with no futher connections; shutting down')
