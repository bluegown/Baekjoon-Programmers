import sys



N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
d = [0] * (N+1)
for i in range(len(arr)):
    d[i+1] = d[i] + arr[i]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(d[j] - d[i-1])

