#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:simple.py
DESC: 使用smtplib.sendmail()发送电子邮件
"""

import sys, smtplib

message_template = """To: {}
From: {}
Subject: Test Message from simple.py

Hello,
This is a test message sent to you from the simple.py programe
in Foundations of python Network programming.
"""

def main():
    if len(sys.argv) < 4:
        name = sys.argv[0]
        print('Usage: {} server fromaddr toaddr [toaddr...]'.format(name))
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template.format(', '.join(toaddrs), fromaddr)
    connection = smtplib.SMTP(server)
    connection.sendmail(fromaddr, toaddrs, message)
    connection.quit()

    s = '' if len(toaddrs) == 1 else 's'
    print("Message sent to {} recipent{}".format(len(toaddrs), s))


if __name__ == "__main__":
    main()
