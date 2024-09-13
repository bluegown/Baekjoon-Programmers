import sys

N = int(input())
arr = []
arr.append(0)
for _ in range(N):
    num = int(input())
    arr.append(num)

d = [0] * (N+1)
if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])
else:
  d[1] = arr[1]
  d[2] = arr[1] + arr[2]
  d[3] = max(arr[1] + arr[3], arr[2] + arr[3])
  for i in range(4,N+1):
      d[i] = max(d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i])

  print(d[N])

