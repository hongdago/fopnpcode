#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName: udp_remote.py
DESC: 运行在不同机器的UDP客户端和服务器
"""

import argparse, random, socket, sys

MAX_BYTES = 65525

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print("Listening at", sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print('Pretendin to drop packet from {}'.format(address))
            continue
        text = data.decode('ascii')
        print('The client at {} say {!r}'.format(address, text))
        message = 'You data war {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    delay = 0.1 #seconds
    text = 'This is another message'
    data = text.encode('ascii')
    while True:
        sock.send(data)
        print('Waiting up to {} senconds for a replay'.format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2 # wait event longer for the next request
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        else:
            break # we are done, and can stop looping

    print('The server says {!r}'.format(data.decode('ascii')))

if __name__ == "__main__":
    choices = {'client' : client, 'server' : server}
    parser = argparse.ArgumentParser(description='Send and receive UDP pretending packets are often dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listend at; host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)

