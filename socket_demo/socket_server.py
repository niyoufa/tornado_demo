#coding=utf-8

import socket

HOST='localhost'
PORT=8085

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind( (HOST,PORT) )

s.listen(1)

while True :
	conn , addr = s.accept()
	print "Connected by " , addr
	while True :
		data = conn.recv(1024)
		conn.sendall(data)

conn.close()