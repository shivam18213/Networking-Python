import math
ip=input().split("/")
output=[]
host=int(input())
host=host+2
zeros=int(math.log(host,2))
end=""
for i in range (0,zeros):
   end=end+'0'
end='1'*(32-len(end))+end
for i in range(0,25,8):
   output.append(int(end[i:i+8],2))
c=0
for i in output:
   c+=1
   if(c<4):
      print(i,end=".")
   else:
      print(i,end="")
