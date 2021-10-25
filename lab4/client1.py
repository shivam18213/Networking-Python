import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
while True:
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  in_data =  client.recv(1024)
  print("Reply From Server to client1: ")
  print(in_data.decode())
  if out_data=='bye':
   break
client.close()
