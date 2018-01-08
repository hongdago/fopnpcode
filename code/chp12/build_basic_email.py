#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:build_basic_email.py
DESC: 生成一个包含简单文本的电子邮件消息
"""

import email.message, email.policy, email.utils, sys

text = """Hello,
This is a basic message from chapter 12.
-- Anonymous"""

def main():
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test sender <sender@example.com>'
    message['Subject'] = 'Test message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()
    message.set_content(text)
    sys.stdout.buffer.write(message.as_bytes())

if __name__ == "__main__":
    main()
