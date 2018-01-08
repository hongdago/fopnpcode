#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:debug.py
DESC: 一个更谨慎的SMTP客户端
"""

import sys, smtplib, socket


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


    try:
        connection = smtplib.SMTP(server)
        connection.set_debuglevel(1)
        connection.sendmail(fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipent{}".format(len(toaddrs), s))
        connection.quit()

if __name__ == "__main__":
    main()
