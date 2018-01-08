#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:open_imaplib.py
DESC: 连接IMAP并列出文件夹
"""

import getpass, imaplib, sys

def main():
    if len(sys.argv) != 3:
        print('Usage: %s hostname username' % sys.argv[0])
        sys.exit(2)

    hostname, username = sys.argv[1:]
    m = imaplib.IMAP4_SSL(hostname)
    m.login(username, getpass.getpass())
    try:
        print('Capabilities:', m.capabilities)
        print('Listing mailboxes ')
        status, data = m.list()
        print('Status:', repr(status))
        print('Data:')
        for datnum in data:
            print(repr(datnum))
    finally:
        m.logout()

if __name__ == "__main__":
    main()
