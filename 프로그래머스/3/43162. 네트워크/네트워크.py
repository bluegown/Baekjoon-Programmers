from collections import deque
def bfs(graph, start, visited):
    visited[start] = True
    
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][j] == 1 and i!=j:
                graph[i+1].append(j+1)
    visited = [False] * (n+1)
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            answer += 1
    
    
    return answer