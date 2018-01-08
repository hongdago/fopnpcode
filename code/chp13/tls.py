#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:tls.py
DESC: 选择性地使用TLS

1、构造SMTP对象
2、发送EHLO命令。如果远程服务器不支持EHLO的话， 那么它也不支持TLS
3、检查s.has_extn(), 查看是否存在starttls, 如果不存在的话，就表示远程服务器不支持TLS，而只能明文发送
4、构造一个SSL上下文对象，验证服务器身份
5、调用starttls(),初始化加密信道
6、再次调用ehlo(),此时它已经是加密
7、最后发送信息
"""


import sys, smtplib, socket, ssl


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
        send_message_securely(connection, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipent{}".format(len(toaddrs), s))
        connection.quit()

def send_message_securely(connection, fromaddr, toaddrs, message):
    code = connection.ehlo()[0]
    uses_temp = (200 <= code <= 299)
    if not uses_temp:
        code = connection.helo()[0]
        if not (200 <= code <= 299):
            print('Remote server refused HELO; code:', code)
            sys.exit(1)

    if uses_temp and connection.has_extn('starttls'):
        print('Negotiating TLS...')
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.set_default_verify_paths()
        context.verify_mode = ssl.CERT_REQUIRED
        connection.starttls(context=context)
        code = connection.ehlo()[0]
        if not(200 <= code <= 299):
            print('Couldn\'t EHLO after STARTTLS')
            sys.exit(1)
        print("Using TLS connection")
    else:
        print("Server does not support TLS; using normal connection")

    connection.sendmail(fromaddr, toaddrs, message)

if __name__ == "__main__":
    main()
