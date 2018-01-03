#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:srv_single.py
DESC: 最简单的可用服务器是单线程的
"""

import zen_utils


if __name__ == "__main__":
    address = zen_utils.parse_command_line('simple single_threaded server')
    listener = zen_utils.create_srv_socket(address)
    zen_utils.accep_connection_foever(listener)
