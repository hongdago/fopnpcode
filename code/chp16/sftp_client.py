#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:sftp_client.py
DESC: 使用SFTP列出目录内容并获取文件
"""

import argparse, functools, paramiko

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

def main(hostname, username, filenames):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username)

    def print_status(filename, bytes_so_far, bytes_total):
        percent = 100. * bytes_so_far / bytes_total
        print('Transfer of %r is at %d/%d bytes (%.1f%%)' % (filename, bytes_so_far, bytes_total, percent))


    sftp = client.open_sftp()
    for filename in filenames:
        if filename.endswith('.copy'):
            continue
        callback = functools.partial(print_status, filename)
        sftp.get(filename, filename+'.copy', callback=callback)
    client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect over SSH')
    parser.add_argument('hostname', help='Remote machine name')
    parser.add_argument('username', help='Username on the remote machine')
    parser.add_argument('filenames', nargs='+', help='filenames to fetch')
    args = parser.parse_args()
    main(args.hostname, args.username, args.filenames)
