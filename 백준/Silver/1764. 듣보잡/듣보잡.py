import sys

N,M = map(int,sys.stdin.readline().split())

lis = set()
wat = set()

for i in range(N):
    name = input()
    lis.add(name)
ans = []

for i in range(M):
    name = input()
    wat.add(name)

for i in lis:
    if i in wat:
        ans.append(i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
            








