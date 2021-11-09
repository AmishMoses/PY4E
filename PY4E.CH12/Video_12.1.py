#!/usr/env/ python
# Sockets in Python
# Python has built in support for TCP sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# mysock.connect ( ( 'Hostname', port#))
