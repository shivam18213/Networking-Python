import socket 

HOST = 'localhost'
PORT=  50007
s= socket.socket()
s.bind((HOST,PORT))
s.listen(1);
print("server listenting..")
MAC=["AB:12:34:2:DE","1A:AE:23:56:7F","12:45:59:ab:cd:67","1:34:7:ef:bc:d2","12:23:56:24:ab:e2","1:e:34:56:34:32","54:e2:f4:d4:fd:e1","21:38:23:12:ab:4","11:23:45:34:11:2e"]
IP=["10.20.30.40","1.23.34.35","10.45.67.78","21.76.34.56","11.43.45.56","10.5.67.234","12.34.62.3","23.6.5.98","11.34.45.67"]
conn,addr=s.accept()

print('connected by',addr)
while True:
 
    data = conn.recv(1024)
    for i in range (9) :
        if IP[i]==data.decode():
             m2="MAC is:  "
             conn.sendall(m2.encode()+MAC[i].encode())
       
        if i==8:
             m1="sorry MAC not found" 
             conn.sendall(m1.encode())
               
        if not data:
          break
conn.close()
 
