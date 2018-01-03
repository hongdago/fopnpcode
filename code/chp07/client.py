#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:client.py
DESC: 用于《Python之禅》示例协议的客户端
"""

import argparse, random, socket, zen_utils 

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return 
    for aphorism in random.sample(aphorisms, 3):
        sock.sendall(aphorism)
        print(aphorism, zen_utils.recv_until(sock, b'.'))
    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostnmae')
    parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port (default 1060)')
    parser.add_argument('-e', action='store_true', help='cause an error')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address, args.e)
