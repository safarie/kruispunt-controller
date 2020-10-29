import socket
import json

host = "127.0.0.1"
port = 54000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
  data = client.recv(1024)
  print(json.loads(data.decode("utf-8")))
