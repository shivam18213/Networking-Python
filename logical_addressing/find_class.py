ip1=input().split(".")
c,f=0,0;
ip2=[]
for bits in ip1:
    c=c+1
    if bits== "":
        print("Invalid")
        f=1
        break
    elif bits=="0" and c==1:
        print("Invalid")
        f=1
        break
    bits=bin(int(bits))
    bits=bits.replace("0b","")
    if len(bits)>8:
        print("Invalid")
        f=1
        break
    bits='0'*(8-len(bits))+bits
    ip2.append(bits)
    if c==4:
        print("Valid")
if f==0 and c==4:
        check=ip2[0]

        if check[0]=='0':
            print('A')
        elif check[0:2]=="10":
            print('B')
        elif check[0:3]=="110":
            print('C')
        elif check[0:4]=="1110":
            print('D')
        elif check[0:5]=="11110":
            print('E')
