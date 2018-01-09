#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:binarydl.py
DESC: 下载二进制文件
"""
import os
from ftplib import FTP

def main():
    if os.path.exists('esep-1.5.tgz'):
        raise IOError('refusing to overwrite your esep-1.5.tgz')

    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel/')

    with open('esep-1.5.tgz', 'wb') as f:
        ftp.retrbinary('RETR esep-1.5.tgz', f.write)
    ftp.quit()


if __name__ == "__main__":
    main()
