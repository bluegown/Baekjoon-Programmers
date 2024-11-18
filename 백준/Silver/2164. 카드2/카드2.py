import sys
from sys import stdin
from collections import deque
N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    elem = queue.popleft()
    queue.append(elem)

lastelem = queue.popleft()
print(lastelem)     