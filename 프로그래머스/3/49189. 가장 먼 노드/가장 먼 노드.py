from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    queue = deque()
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    queue.append(1) # 시작점 넣기
    distance[1] = 1
    while queue:
        now = queue.popleft() # 큐에서 값을 꺼낸다
        for i in graph[now]:
            if distance[i] == 0:
                queue.append(i)
                distance[i] = distance[now] + 1
    print(distance)
    
    return distance.count(max(distance))