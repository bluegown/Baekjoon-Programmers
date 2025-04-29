import sys
import heapq
from collections import deque
INF = 1e9

def bfs(graph,start):
    distance[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        element = queue.popleft()
        for i in graph[element]:
            if distance[i] == INF:
                distance[i] = distance[element] + 1
                queue.append(i)



N,M,K,X = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M): 
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)

distance = [INF] * (N+1)

bfs(graph,X)

ans = []
for i in range(len(distance)):
    if distance[i] == K:
        ans.append(i)
ans.sort()
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)






