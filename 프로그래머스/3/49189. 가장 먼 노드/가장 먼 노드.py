from collections import deque
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    dist = [0] * (n+1)
    
    queue = deque()
    queue.append(1)
    dist[1] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] == 0:
                dist[i] = dist[v] + 1
                queue.append(i)
    
    return dist.count(max(dist))