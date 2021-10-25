n= int(input())
data=[]
for j in range (0,n):
   values=input()
   data.append(int(values,2))
   l=len(values)
s=int('0',2)
for i in data:
   s =s+i
extra=" "
if len(bin(s))-l > 2 :
       s=bin(s)
       extra = s[2:len(s)-l]
       s=s[len(s)-l:]
s = bin(int(s,2)+int(extra,2))
if (l-(len(s)-2))>0:
   s=s[2:]
   s=((l-(len(s)))*'0')+s
s2=""
for digit in s:
   if digit=='0':
      s2=s2+'1'
   else:
      s2=s2+'0'
print(s2)

