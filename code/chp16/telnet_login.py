#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:telnet_login.py
DESC: 使用Telnet登录远程主机
"""

import argparse, getpass, telnetlib

def main(hostname, username, password):
    t = telnetlib.Telnet(hostname)
    #t.set_debuglevel(1)
    t.read_util(b'login')
    t.write(username.encode('utf-8'))
    t.write(b'\r')
    t.read_until(b'assword')  # first letter mighe be 'p' or 'P'
    t.write(password.encode('utf-8'))
    t.write(b'\r')
    n, match, previours_text = t.expect([br'Login incorrect', br'\$'], 10)
    if n == 0:
        print('Username and password failed - giving up')
    else:
        t.write(b'exec uptime\r')
        print(t.read_all().decode('utf-8'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use Telent to log in')
    parser.add_argument('hostname', help='Remote host to telnet to')
    parser.add_argument('username', help='Remote usernmae')
    args = parser.parse_args()
    password = getpass.getpass("Password: ")
    main(args.hostname, args.username, password)
