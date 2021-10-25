n= int(input())
data_list=[]
for data in range(0,n):
 data= input()
 data_list.append(data)
count=0
dist=8
for i in range(0,n):
 for j in range(i+1,n):
  for position in range(0,len(data_list[i])):
   if data_list[i][position]!=data_list[j][position] :
    count+=1
  if count<dist:
   dist=count
  count=0
print(dist)
