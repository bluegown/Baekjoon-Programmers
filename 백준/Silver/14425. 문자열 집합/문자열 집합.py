import sys

N,M = map(int,sys.stdin.readline().split())

answer = 0
dic = set()

for i in range(N):
    st = input()
    dic.add(st)

for j in range(M):
    st = input()
    if st in dic:
        answer += 1
print(answer)