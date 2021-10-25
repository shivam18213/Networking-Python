n=int(input())
l=[]
for i in range (n):
    bit=input().split(",")
    l.append(bit)
r=input().split(",")
l1=[]
l2=[]
l3=[]
for i in range(0,n,1):
    sum=0
    for j in range(4):
        temp=(int(l[i][j]))*(int(r[j]))
        l1.append(temp)
        sum=sum+int(temp)
    sum=int(sum/4)
    l2.append(sum)
for i in l2:
    if(i==-1):
        print('0')
    elif(i==0):
        print('-')
    else:
        print('1')
