#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:advbinarydl.py
DESC: 提供状态更新的二进制下载
"""

import os, sys
from ftplib import FTP

def main():
    if os.path.exists('LFSBOOK_ED1.iso'):
        raise IOError('refusing to overwrite your LFSBOOK_ED1.iso file')

    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel')
    ftp.voidcmd("TYPE I")

    socket, size = ftp.ntransfercmd("RETR LFSBOOK_ED1.iso")
    nbytes = 0

    f = open('LFSBOOK_ED1.iso', 'wb')

    while True:
        data = socket.recv(2048)
        if not data:
            break
        f.write(data)
        nbytes += len(data)
        print('\rReceived', nbytes, end=' ')
        if size:
            print("of %d total bytes (%.1f%%)" % (size, 100. * nbytes / float(size)), end=' ')
        else:
            print("bytes", end=' ')
        sys.stdout.flush()

    print()
    f.close()
    socket.close()
    ftp.voidresp()
    ftp.quit()

if __name__ == "__main__":
    main()
