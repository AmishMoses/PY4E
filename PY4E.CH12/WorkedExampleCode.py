#!/usr/env/ python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # This is a function call with a tuple inside
# mysock.connect ( ( 'Hostname', port#))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# .encode() converts from unicode (inside python) to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
# decode() converts it back to unicode for python to read
mysock.close()