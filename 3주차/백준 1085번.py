x,y,w,h=map(int,input().split())
min = 0
if x<(w/2):
  min=x
else :
  min=w-x
if y<(h/2) and y < min:
  min = y
else:
  if (h-y)<min:
    min=h-y

print(min)
