#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:ehlo.py
DESC: 检查消息的大小限制
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
        report_on_message_size(connection, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipent{}".format(len(toaddrs), s))
        connection.quit()

def report_on_message_size(connection, fromaddr, toaddrs, message):
    code = connection.ehlo()[0]
    uses_temp = (200 <= code <= 299)
    if not uses_temp:
        code = connection.helo()[0]
        if not (200 <= code <= 299):
            print('Remove server refused HELLO;code:', code)
            sys.exit(1)
    if uses_temp and connection.has_extn('size'):
        print("Maxinum message size is", connection.esmtp_features['size'])
        if len(message) > int(connection.esmtp_features['size']):
            print('Message too large; aborting')
            sys.exit(1)

    connection.sendmail(fromaddr, toaddrs, message)
    

if __name__ == "__main__":
    main()
