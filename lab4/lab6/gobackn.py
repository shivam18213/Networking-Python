inputs=[]
sf=[]
sn=[]
n=int(input())
for i in range(0,n):
    l=input().split()
    l=[int(i) for i in l]
    inputs.append(l)
for l in inputs:
    sw=(pow(2,l[0])-1)
    if l[3] != 0:
        sf.append(l[1])
        sn.append(l[2])
    elif l[4]!=0:
        if (l[4]>sw):
            sf.append(l[1])
            sn.append(l[1]+sw)
        else:
            sf.append(l[1])
            sn.append(l[2]+l[4])
    elif l[5]!=0:
        if (l[5]>0):
            sf.append(l[5])
            sn.append(l[2])
        else:
            sf.append(-1*l[5])
            sn.append(l[2])
for i in range(0,n):
    print(sf[i],sn[i])
