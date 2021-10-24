import socket
HOSTP = ('localhost',50007 )    
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


msg=input("Enter the ip address")
while msg!="bye":
	s.sendto(msg.encode(),HOSTP)
	data,address = s.recvfrom(1024)
	print('MAC is: '+data.decode())
	msg=input("Enter the ip address")
s.close()

