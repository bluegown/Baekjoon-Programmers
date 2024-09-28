import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
count = 1
elem = arr[0]
d = [1] * (N+1)
for i in range(1,N):
    for j in range(i):
      if arr[i] > arr[j]:
         if d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))

         

