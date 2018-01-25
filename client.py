# -*- coding: UTF-8 -*-

import socket

host = '127.0.0.1'
port = 15809

s = socket.socket()
s.connect((host, port))
data='./images/0.jpg'
s.send(data)
buffersize = 1024
response=s.recv(buffersize)
print 'response: ',response
s.close()