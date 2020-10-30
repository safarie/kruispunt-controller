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
		updateLight(stage)
		size = len(str(data).replace(" ",""))
		client.send(bytes(str(size) + ":", "utf-8") + bytes(json.dumps(data).replace(" ",""), "utf-8"))
		time.sleep(15)
		if stage >= 4:
			stage = 1
		else:
			stage += 1
	else:
		client.close()
