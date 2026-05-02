from collections import deque
def bfs(graph, distance):
    queue = deque()
    queue.append(1)
    distance[1] = 0
    while queue:
        elem = queue.popleft()
        for i in graph[elem]:
            if distance[i] == 1e9: # 미방문 노드들에 대해 처리
                distance[i] = distance[elem] + 1
                queue.append(i)
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    bfs(graph, distance)
    distance[0] = 0
    return distance.count(max(distance))