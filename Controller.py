import socket
import threading

from Functions import *
host = "127.0.0.1"
port = 54000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("waiting for client")

while True:
	client, addr = server.accept()
	recv_thread = threading.Thread(target=receiving, args=(client,))
	recv_thread.start()
	
	while True:		
		if not getSmart():
			if getStage('r') < 14:
				s = getStage('r') + 1
				setStage(s, s)
			else:
				setStage(1, 1)
		else:
			SmartLights()
		
		update()
		
		size = len(str(data).replace(" ",""))
		client.send(bytes(str(size) + ":", "utf-8") + bytes(json.dumps(data).replace(" ",""), "utf-8"))
		
		time.sleep(getTime())
		
	else:
		client.close()
			
server.close()
print("server closed")
