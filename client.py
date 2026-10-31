import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
s.sendall('Hello, MAZAFAKA!'.encode('utf-8'))
data = s.recv
s.close