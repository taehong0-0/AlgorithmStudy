n=int(input())
list_n=list(map(int,input().split()))
m=int(input())
list_m=list(map(int,input().split()))
list_n.sort()
for i in range(m):
  answer=0
  num=list_m[i]
  start=0
  end=n-1
  while(start<=end):
    mid=int((start+end)/2)
    if list_n[mid]<num:
      start=mid+1
    elif list_n[mid]>num:
      end=mid-1
    else:
      answer=1
      break
  print(answer)
