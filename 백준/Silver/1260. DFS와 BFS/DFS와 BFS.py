import sys
from collections import deque
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end = ' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)
def bfs(graph,v,visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        elem = queue.popleft()
        print(elem,end = ' ')
        for i in graph[elem]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
     a,b = map(int,sys.stdin.readline().split())
     graph[a].append(b)
     graph[b].append(a)
for i in graph:
    i.sort()
visited = [False] * (N+1)
dfs(graph,V,visited)
visited = [False] * (N+1)
print()
bfs(graph,V,visited)