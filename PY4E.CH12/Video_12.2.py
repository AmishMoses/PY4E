#!/usr/env python
# Hypertext Transport Protocol
''' You can log onto a sever manually using telnet
telnet data.pr4e.org 80
GET http://data.pr4e.org/page1.htm HTTP/1.0'''
# An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# mysock.connect ( ( 'Hostname', port#))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() 
# \r\n is just saying enter newline 
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()