#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:ssh_commands.py
DESC: 运行独立的SSH命令
"""

import argparse, paramiko

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

def main(hostname, username):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username)
    for command in 'echo "hello world" ', 'uname', 'uptime':
        stdin, stdout, stderr = client.exec_command(command)
        stdin.close()
        print(repr(stdout.read()))
        stdout.close()
        stderr.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connect over SSH')
    parser.add_argument('hostname', help='Remote machine name')
    parser.add_argument('username', help='Username on the remote machine')
    args = parser.parse_args()
    main(args.hostname, args.username)
