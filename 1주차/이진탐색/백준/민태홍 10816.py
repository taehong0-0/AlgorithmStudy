from collections import Counter
n=int(input())
list_n=list(map(int,input().split()))
m=int(input())
list_m=list(map(int,input().split()))
list=Counter(list_n)
for i in list_m:
  print(list[i])