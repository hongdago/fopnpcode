#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:wsgi_env.py
DESC: 以WSGI应用程序形式编写的简单HTTP服务

    WSGI应用程序是可以被调用的， 并且有两个输入参数。 
    第一个参数是:environ, 用于接受一个字典
    第二个参数也是可以被调用的，习惯上会将其命名为start_response
    WSGI通过start_response()来声明相应头信息
"""

from pprint import pformat
from wsgiref.simple_server import make_server

def app(environ, start_response):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    start_response('200 OK', list(headers.items()))
    yield 'Here is the WSGI environment:\r\n\r\n'.encode('utf-8')
    yield pformat(environ).encode('utf-8')

if __name__ == "__main__":
    httpd = make_server('', 8000, app)
    host, port = httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()
