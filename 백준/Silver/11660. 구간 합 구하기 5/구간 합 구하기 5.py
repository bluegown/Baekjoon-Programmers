import sys

N,M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
d = [[0] * (N+1) for _ in range (N+1)]
sum = 0
d[1][1] = arr[0][0]
for i in range(1,N+1):
   d[1][i] = d[0][i-1]+ arr[0][i-1]

for i in range(1,N+1):
    sum = 0
    for j in range(1,N+1):
          sum += arr[i-1][j-1]
          d[i][j] = d[i-1][j] + sum


for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1])
        
