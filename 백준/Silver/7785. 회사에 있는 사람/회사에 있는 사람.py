import sys

N = int(input())
s = set()
for i in range(N):
    n, x = sys.stdin.readline().split()
    if x == 'enter':
        s.add(n)
    if x == 'leave':
        if n in s:
            s.remove(n)
ans = []
for i in s:
    ans.append(i)
ans.sort(reverse = True)
for i in ans:
    print(i)

