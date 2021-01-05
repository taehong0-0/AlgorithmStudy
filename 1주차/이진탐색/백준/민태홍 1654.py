lan_num,num=map(int,input().split())
num_list=[]
for _ in range(lan_num):
  num_list.append(int(input()))
start,end=1,max(num_list)
while start<=end:
  answer=0
  mid=(start+end)//2
  for j in num_list:
    answer+=j//mid
  if answer<num:
    max_num=end
    end=mid-1
  else:
    start=mid+1
print(end)