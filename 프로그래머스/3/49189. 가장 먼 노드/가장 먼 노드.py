from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = [0] * (n+1)
    distance[1] = 1
    
    queue = deque()
    queue.append(1)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == 0:
                distance[i] = distance[v] + 1
                queue.append(i)
    
    return distance.count(max(distance))