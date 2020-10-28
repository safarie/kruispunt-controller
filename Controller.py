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

# while True:
# 	updateLight(1)
# 	print(data)
# 	time.sleep(2)
# 	updateLight(2)
# 	print(data)
# 	time.sleep(2)
# 	updateLight(3)
# 	print(data)
# 	time.sleep(2)
# 	updateLight(4)
# 	print(data)
# 	time.sleep(2)

while True:
	client, addr = server.accept()
	client.send(bytes(json.dumps(data), "utf-8"))
	client.close()