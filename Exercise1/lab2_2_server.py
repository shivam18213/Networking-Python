import socket 

HOST = 'localhost'
PORT=  50007
s= socket.socket()
s.bind((HOST,PORT))
s.listen(1);
print("server listenting..")
DOMAIN=["www.google.com","www.gmail.com","www.linkedin.com","www.youtube.com","www.vit.ac.in","www.india.gov.in","www.researchgate.in","www.yahoo.com","www.facebook.com"]
IP=["10.20.30.40","1.23.34.35","10.45.67.78","21.76.34.56","11.43.45.56","10.5.67.234","12.34.62.3","23.6.5.98","11.34.45.67"]
conn,addr=s.accept()

print('connected by',addr)
while True:
 
    data = conn.recv(1024)
    for i in range (9) :
        if not data:
          break
        if DOMAIN[i]==data.decode():
             m2="IP is:  "
             conn.sendall(m2.encode()+IP[i].encode())

        if i==8 :
             m1="sorry Domain not found" 
             conn.sendall(m1.encode())
                       
conn.close()
 
