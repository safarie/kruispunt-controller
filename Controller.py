import socket
import json
import time

from Functions import *

host = "127.0.0.1"
port = 54000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("waiting for client")

go = True
stage = 1

while True:
	client, addr = server.accept()
	while go:
		size = len(str(data).replace(" ",""))
		client.send(bytes(str(size) + ":", "utf-8") + bytes(json.dumps(data).replace(" ",""), "utf-8"))
		
		if stage % 2 == 1:
			updateLightR(1)
			updateLightL(1)
		else:
			updateLightR(stage)
			updateLightL(stage)
		
		if stage < 8:
			stage += 1
		else:
			stage = 1
		
		time.sleep(5)
	else:
		client.close()
