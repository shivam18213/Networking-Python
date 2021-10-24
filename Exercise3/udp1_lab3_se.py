import socket
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
f=open("data1.txt","r")
l1=[]
l2=[]
i=0
for line in f:
   for word in line.split():
      if(i%2==0):
        l1.append(word)
      else:
        l2.append(word)
      i+=1
f.close()
while True:
    i=0
    data,address = s.recvfrom(1024)
    for i in range(0,9):
       if data.decode()==l1[i]:
          s.sendto(l2[i].encode(),address)
          print(i)
          break
    if (i==8):
       comment="sorry MAC not found"
       s.sendto(comment.encode(),address)
    elif not data:
       break
    i=0
s.close()



