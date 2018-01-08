#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:mailbox.py
DESC: 使用POP的list命令
"""


import getpass, poplib, sys

def main():
    if len(sys.argv) !=3:
        print('Usage: %s hostname username ' % sys.argv[0])
        exit(2)

    hostname, username = sys.argv[1:]
    passwd = getpass.getpass()

    p = poplib.POP3_SSL(hostname)
    try:
        p.user(username)
        p.pass_(passwd)
    except poplib.error_proto as e:
        print("Login failed:", e)
    else:
        response, listings, octet_count = p.list()
        if not listings:
            print('No messages')
        for listing in listings:
            number, size = listing.decode('ascii').split()
            print('Message %s hav %s bytes ' % (number, size))
    finally:
        p.quit()

if __name__ == "__main__":
    main()
