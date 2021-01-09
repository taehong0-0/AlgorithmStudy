import sys
input = sys.stdin.readline
tree_num,num=map(int,input().split())
num_list=list(map(int,input().split()))
start,end=1,max(num_list)

while start<=end:
  answer=0
  mid=(start+end)//2

  for j in num_list:
    if j>mid:
       answer+= j-mid

  if answer<num:
    end=mid-1
  else:
    start=mid+1

print(end)