import sys
from collections import deque
import heapq
INF = 1e9
def bfs(graph,distance,start,visited):
    global res
    q = []
    heapq.heappush(q,(0,start)) # cost, now
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                visited[i[0]] = True
                heapq.heappush(q,(cost,i[0]))
                


    
T = int(input())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    res = 1e9
    for _ in range(M):
        x,y = map(int,sys.stdin.readline().split())
        graph[x].append((y,1))
        graph[y].append((x,1))
    print(N-1)

    
