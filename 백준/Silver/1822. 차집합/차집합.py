import sys

N,M = map(int,sys.stdin.readline().split())

a = set(list(map(str,sys.stdin.readline().split())))

b = set(list(map(str,sys.stdin.readline().split())))
ans = []
for i in a:
    if i not in b:
        ans.append(i)
ans = list(map(int,ans))
ans.sort()
ans = list(map(str,ans))
print(len(ans))
if len(ans) > 0:
    print(' '.join(ans))