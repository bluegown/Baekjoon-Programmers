import sys
from collections import deque
N = int(input())


queue = deque(enumerate(map(int,sys.stdin.readline().split())))


ans = []

while queue:
    index, jump = queue.popleft()
    ans.append(index + 1) # 방문 순서
    if jump > 0:
        queue.rotate(-jump + 1) # (jump -1 ) 만큼만 땡겨와야됨.. 이미 Popleft 조져서
    else:
        queue.rotate(-jump)
    

for i in ans:
    print(i,end=' ')