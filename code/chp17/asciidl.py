#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:asciidl.py
DESC: 下载ASCII文件
"""

import os
from ftplib import FTP

def main():
    if os.path.exists('README'):
        raise IOError('refusing to overwrite your README file')

    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel')
    with open('README', 'w') as f:
        def writeline(data):
            f.write(data)
            f.write(os.linesep)
        ftp.retrlines('RETR README', writeline)
    ftp.quit()

if __name__ == "__main__":
    main()
