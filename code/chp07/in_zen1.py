#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:in_zen1.py
DESC: 相应一个将套接字连接到stdin/stdout/stderr的客户端
"""

import socket, sys, zen_utils

if __name__ == "__main__":
    sock = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('log.txt', 'a', buffering=1)
    address = sock.getpeername()
    print('Accept connection from {}'.format(address))
    zen_utils.handle_conversation(sock, address)
