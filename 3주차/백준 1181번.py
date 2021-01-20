n=int(input())
l = []
for _ in range(n):
  word=input()
  if word not in l:
    l.append(word)  
ans=[]
new=[]
length=0
for i in range(50):
  for k in range(len(l)):
    if len(l[k]) ==i:
      new.append(l[k])
      length+=1
  new.sort()
  for a in new:
    ans.append(a)
  new=[]
  if length==len(l):
    break
for w in ans:
  print(w)
  