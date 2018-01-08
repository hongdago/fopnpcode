#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:build_mime_email.py
DESC: 构造包含HTML、内嵌图片以及附件的MIME格式电子邮件
"""

import argparse, email.message, email.policy, email.utils, mimetypes, sys

plain = """Hello,
 This is a basic message from chapter 12.
 -- Anonymous"""

html = """<p> Hello, </p>
<p> This is a  <b>test message</b> from Chapter 12.</p>
<p>- <i>Anonymous</i></p>"""

img = """<p> This is smallest possible blue GIF:</p>
<img src="cid:{}" height="80", width="80">"""

#Tiney example GIF from http://www.perlmonks.org/?node_id=7974
blue_dot = (b'GIF89a1010\x900000\xff000,000010100\x02\x02\x0410;'.replace(b'0',b'\x00').replace(b'1',b'\x01'))

def main(args):
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test sender <sender@example.com>'
    message['Subject'] = 'Test message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()

    if not args.i:
        message.set_content(html, subtype='html')
        message.add_alternative(plain)
    else:
        cid = email.utils.make_msgid()
        message.set_content(html + img.format(cid.strip('<>')), subtype='html')
        message.add_related(blue_dot, 'image', 'gif', cid=cid, filename='blue-dot.gif')
        message.add_alternative(plain)

    for filename in args.filenames:
        mime_type, encoding = mimetypes.guess_type(filename)
        if encoding or (mime_type is None):
            mime_type = 'application/octet-stream'
        main, sub = mime_type.split('/')
        if main == 'text':
            with open(filename, encoding='utf-8') as f:
                text = f.read()
            message.add_attachment(text, sub, filename=filename)
        else:
            with open(filename, 'rb') as f:
                data = f.read()
            message.add_attachment(data, main, sub, filename=filename)

    sys.stdout.buffer.write(message.as_bytes())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build ,print a MIME email')
    parser.add_argument('-i', action='store_true', help='Include GIF image')
    parser.add_argument('filenames', nargs='*', help='Attachment filename')
    main(parser.parse_args())
