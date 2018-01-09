#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:connect.py
DESC: 建立简单的FTP连接

FTP服务器下载文件的传统操作过程(主动模式)
1、首先，FTP客户端发起一条连接命令，连接至服务器上的一个FTP端口
2、客户端通过认证（通常是通过用户名和密码来认证)
3、客户端通过改变服务器上的目录来上传或者获取想要的文件
4、客户端在一个新的数据连接的端口上开始监听，并将监听号告知服务器
5、服务器连接到客户端打开的这个端口
6、传输文件
7、关闭数据连接

（被动模式，FTP客户端的默认默认模式）
4、服务器开启另一个端口，并将端口号告知客户端，客户端发起第二个连接。

"""

from ftplib import FTP

def main():
    ftp = FTP('ftp.ibiblio.org')
    print('Welcome:', ftp.getwelcome())
    ftp.login()
    print('Current working directory:', ftp.pwd())
    ftp.quit()

if __name__ == "__main__":
    main()
