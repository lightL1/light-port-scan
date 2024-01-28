import socket
import os
import time
print("bem vindo ao meu propio port scanner meus caros thanks!!")
site = input("digite site alvo:")

ports = [21,22,80,443,445,3306,25]

for port in ports:
	print(port)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex((site, port)) 
	if code == 0:
		print(port, "OPEN")
	else:
		print("closed")
