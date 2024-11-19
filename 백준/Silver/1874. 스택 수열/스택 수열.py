import sys
from collections import deque
N = int(input())

stack = []
answer = []
flag = False
cur = 1
for _ in range(N):
    element = int(sys.stdin.readline())

    while cur <= element:
        stack.append(cur)
        answer.append('+')
        cur += 1 # 현재 인덱스까지 push
    if stack[-1] == element: # 만약 천장이랑 현재 입력받은 수가 같다면
        stack.pop()
        answer.append('-') # 머리 제거
    else:
        flag = True
        print('NO')
        break

if not flag:
        for i in answer:
            print(i)

    