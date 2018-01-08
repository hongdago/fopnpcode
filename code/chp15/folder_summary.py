#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:folder_summary.py
DESC: 下载文件夹中的所有消息
"""
import getpass, sys, email
from imapclient import IMAPClient

def main():
    if len(sys.argv) != 4:
        print('Usage: %s hostname username foldername' % sys.argv[0])
        sys.exit(2)

    hostname, username, foldername = sys.argv[1:]
    c = IMAPClient(hostname, ssl=True)
    try:
        c.login(username, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        print_summary(c, foldername)
    finally:
        c.logout()

def print_summary(c, foldername):
    c.select_folder(foldername, readonly=True)
    msgdict = c.fetch('1:*', ['BODY.PEEK[]'])
    for message_id, message in list(msgdict.items()):
        e = email.message_from_string(message['BODY[]'])
        print(message_id, e['From'])
        payload = e.get_payload()
        if isinstance(payload, list):
            part_content_types = [ part.get_content_type() for part in payload]
            print(' Parts:', ' '.join(part_content_types))
        else:
            print(' ', ' '.join(payload[:60].split()), '...')

if __name__ == "__main__":
    main()
