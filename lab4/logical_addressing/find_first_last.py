import math
ip=input()
le=ip[-2:]
le=int(le)
n=32-le
n1=math.pow(2,n)
if(le>=24):
    l=len(ip)
    a=ip[:l-5]
    fa=a+'0'
    la=a+'63'
    print(fa)
    print(la)
    print(int(n1))
elif(le>=8 and le<16):
    l=len(ip)
    a=ip[:l-11]
    fa=a+'0.0.0'
    l1=str(n1-1)
    la=a+'255.255.255'
    print(fa)
    print(la)
    print(int(n1))
elif(le>=16 and le<24):
    l=len(ip)
    a=ip[:l-8]
    fa=a+'0.0'
    l1=str(n1-1)
    la=a+'255.255'
    print(fa)
    print(la)
    print(int(n1))
