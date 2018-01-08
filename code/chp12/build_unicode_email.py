#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:build_unicode_email.py
DESC: 邮件头编码
"""

import email.message, email.policy, sys

text = """\
        你是谁？
        你从哪里来， 要到哪里去？"""


def main():
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = '角落 <recipoent@example.com>'
    message['From'] = '远方 <sender@example.com>'
    message['Subject'] = 'Two lines from the Wanderer'
    message['Date'] = email.utils.formatdate(localtime=True)
    message.set_content(text, cte='quoted-printable')
    sys.stdout.buffer.write(message.as_bytes())

if __name__ == "__main__":
    main()
