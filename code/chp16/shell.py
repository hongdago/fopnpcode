#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:shell.py
DESC: 支持以空格来分隔参数的shell
"""

import subprocess

def main():
    while True:
        args = input('] ').strip().split()
        if not args:
            pass
        elif args == ['exit']:
            break
        elif args[0] == 'show':
            print('Arguments:', args[1:])
        else:
            try:
                subprocess.call(args)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
