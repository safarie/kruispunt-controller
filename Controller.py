import socket
import json

host = "127.0.0.1"
port = 54000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("waiting for client")

data = {
	"A1-1": 1,
	"A1-2": 1,
	"A1-3": 0,
	"B1-1": 0,
	"B1-2": 0,
	"F1-1": 0,
	"F1-2": 0,
	"V1-1": 0,
	"V1-2": 0,
	"V1-3": 0,
	"V1-4": 0,
	"A2-1": 1,
	"A2-2": 1,
	"A2-3": 0,
	"A2-4": 0,
	"F2-1": 0,
	"F2-2": 0,
	"V2-1": 0,
	"V2-2": 0,
	"V2-3": 1,
	"V2-4": 1,
	"A3-1": 0,
	"A3-2": 0,
	"A3-3": 1,
	"A3-4": 1,
	"A4-1": 0,
	"A4-2": 0,
	"A4-3": 1,
	"A4-4": 1,
	"B4-1": 0,
	"F4-1": 0,
	"F4-2": 0,
	"V4-1": 0,
	"V4-2": 0,
	"V4-3": 0,
	"V4-4": 0,
	"A5-1": 0,
	"A5-2": 0,
	"A5-3": 0,
	"A5-4": 0,
	"F5-1": 0,
	"F5-2": 0,
	"V5-1": 0,
	"V5-2": 0,
	"V5-3": 1,
	"V5-4": 1,
	"A6-1": 1,
	"A6-2": 1,
	"A6-3": 1,
	"A6-4": 1
}

while True:
    client, addr = server.accept()
    client.send(bytes(json.dumps(data), "utf-8"))
    client.close()
    
