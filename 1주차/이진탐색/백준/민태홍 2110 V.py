house,num=map(int,input().split())
num_list=[]
for _ in range(house):
  num_list.append(int(input()))
num_list.sort()
start,end=1,num_list[house-1]-num_list[0]

while start<=end:
  answer=1
  mid=(start+end)//2
  h=num_list[0]
  for j in range(house):
    if num_list[j]>=h+mid:
      answer+=1
      h=num_list[j]
  
  if answer<num:
    end=mid-1
  else:
    result=mid
    start=mid+1
print(result)