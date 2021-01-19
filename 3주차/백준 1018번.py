N,M=map(int,input().split())

board=[]
for _ in range(N):
  board.append(input())
size_N=N-7
size_M=M-7
cnt_list=[]
for i in range(size_N):
  for j in range(size_M):
    count=0
    if(board[i][j]=='B'):
      for p in range(8):
        for k in range(0,8,2):
          if(p%2==0):
            if board[i+p][j+k]!='B' :
              count+=1
            if board[i+p][j+k+1]!='W':
              count+=1
          else :
            if board[i+p][j+k]!='W':
              count+=1
            if board[i+p][j+k+1]!='B':
              count+=1
    else :
      for p in range(8):
        for k in range(0,8,2):
          if(p%2==0):
            if board[i+p][j+k]!='W':
              count+=1
            if board[i+p][j+k+1]!='B':
              count+=1
          else :
            if board[i+p][j+k]!='B':
              count+=1
            if board[i+p][j+k+1]!='W':
              count+=1
    if count > 32:
      count=64-count
    cnt_list.append(count) 
print(min(cnt_list))
