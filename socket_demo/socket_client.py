#coding=utf-8

import socket

HOST='localhost'
PORT=8085

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect( (HOST,PORT) )

while True :
 	cmd  = raw_input("Please input cmd :")
 	s.sendall(cmd)
 	data = s.recv(1024)
 	print data
conn.close()