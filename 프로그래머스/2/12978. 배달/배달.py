import heapq
INF = 1e9
def dijkstra(start , distance, graph):
    q = []
    heapq.heappush(q,(0,start)) # 비용과 노드로 시작
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 최적화가 되어있으므로 Pass
            continue
        for i in graph[now]: # i에선 i[0]가 노드, i[1]이 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    
    for a,b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    distance = [INF] * (N+1)
    
    dijkstra(1 , distance, graph)
    for i in distance:
        if i <= K:
            answer += 1 
    return answer