import sys


N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

d = [1000001] * (N)


d[0] = 0
for i in range(1,N):
    for j in range(0,i):
        value = max((i-j) * (1 + abs(arr[i] - arr[j])),d[j])
        # 얘가 최소한 드는 힘이 될 것
        d[i] = min(d[i],value)
print(d[N-1])
