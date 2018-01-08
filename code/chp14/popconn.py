#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:popconn.py
DESC: 一个非常简单的POP会话
"""

import getpass, poplib, sys

def main():
    if len(sys.argv) !=3:
        print('Usage: %s hostname username ' % sys.argv[0])
        exit(2)

    hostname, username = sys.argv[1:]
    passwd = getpass.getpass()

    p = poplib.POP3_SSL(hostname)
    print('Attempting APOP authentiaction')
    try:
        p.apop(username, passwd)
    except poplib.error_proto:
        print('Attempting standard authentiaction')
        try:
            p.user(username)
            p.pass_(passwd)
        except poplib.error_proto as e:
            print('login failed:', e)
            sys.exit(1)
        else:
            status = p.stat()
            print('You have %d message totaling %d bytes' % status)
    else:
        status = p.stat()
        print('You have %d message totaling %d bytes' % status)
    finally:
        p.quit()

if __name__ == "__main__":
    main()
