def subs(x,y):
   part=""
   for i in range (1,len(y)):
      if x[i]==y[i]:
         part=part+'0'
      else:
         part=part+'1'
   return part;
n1=str(input())
n2=str(input())
div1=bin(int(n1,2))
div1=div1[2:]
n1=n1+(len(n2)-1)*'0'
n1=int(n1,2)
n2=int(n2,2)
div=bin(n1)
div=div[2:]
str2=""
n2=str(bin(n2))
n1=str(bin(n1))
str1=n1[2:len(n2)]
n1=n1[len(n2):]
n2=n2[2:]
str2=subs(str1,n2)
for i in range (0,len(str(div))-len(n2)):
   str2=str2+n1[i]
   if str2[0]=='1':
      str2=subs(str2,n2)
   else:
      str2=subs(str2,len(n2)*'0')
print(div1+str2)
