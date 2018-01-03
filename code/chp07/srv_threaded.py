#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:srv_threaded.py
DESC: 多线程服务器
"""

import zen_utils
from threading import Thread

def start_threads(listener, workers=4):
    t = (listener,)
    for _ in range(workers):
        Thread(target=zen_utils.accep_connection_foever, args=t).start()


if __name__ == "__main__":
    address = zen_utils.parse_command_line('multi-threaded server')
    listener = zen_utils.create_srv_socket(address)
    start_threads(listener)
