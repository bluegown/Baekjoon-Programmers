import sys
from collections import deque
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
visited = [False] * (N+1)
bfs(graph,1,visited)
print(visited.count(True) - 1)
