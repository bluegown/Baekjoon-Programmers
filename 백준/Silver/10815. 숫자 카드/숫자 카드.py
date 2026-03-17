import sys

answer = 0
N = int(input())
list1 = set(list(map(int,sys.stdin.readline().split())))
M = int(input())
list2 = list(map(int,sys.stdin.readline().split()))

ans = []
for i in list2:
    if i in list1:
        ans.append('1')
    else:
        ans.append('0')
print(' '.join(ans))

