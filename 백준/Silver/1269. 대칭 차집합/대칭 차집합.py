import sys

answer = 0
N,M = map(int,sys.stdin.readline().split())

list1 = set(list(map(int,sys.stdin.readline().split())))

list2 = set(list(map(int,sys.stdin.readline().split())))

for i in list1:
    if i not in list2:
        answer += 1
for i in list2:
    if i not in list1:
        answer += 1
print(answer)


