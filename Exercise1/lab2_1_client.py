import socket

HOST = 'localhost'    
PORT = 50007              
s = socket.socket()
s.connect((HOST, PORT))
msg=input("Enter the IP Address: ")
s.sendall(msg.encode())
data = s.recv(1024)
s.close()
print(data.decode())

