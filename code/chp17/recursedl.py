#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:recursedl.py
DESC: 尝试递归的访问目录
"""

from ftplib import FTP, error_perm

def walk_dir(ftp, dirpath):
    original_dir = ftp.pwd()
    try:
        ftp.cwd(dirpath)
    except error_perm:
        return

    print(dirpath)
    names = sorted(ftp.nlst())
    for name in names:
        walk_dir(ftp, dirpath+"/"+name)
    ftp.cwd(original_dir)  # return to cwd of our caller

def main():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    walk_dir(ftp, '/pub/linux/kernel')
    ftp.quit()

if __name__ == "__main__":
    main()
