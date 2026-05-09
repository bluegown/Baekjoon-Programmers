import heapq
def dijkstra(start, graph, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start)) # 비용과 노드로 시작
    
    while q:
        dist, now = heapq.heappop(q) # 비용, 노드 원소 빼고
        if dist > distance[now]: # start node -> 현재 목표 node로
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))         

def solution(n, s, a, b, fares):
    # 개수, 출발 지점, a도착, b도착 , (c -> d가 f비용)
    answer = 1e9
    # 합승하지 않는 경우
    # 합승하고 A를 먼저 내려주는 경우
    # 합승하고 B를 먼저 내려주는 경우 3가지중 min값
    graph = [[] for _ in range(n+1)]
    dist = [[1e9] * (n+1) for _ in range(n+1)]
    # distance[a][b] . a -> b에 대한 값을 표현해보자. 
                
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f)) # 양방향 노드이므로 2개 추가
        
    for start in range(1, n + 1):
        distance = [1e9] * (n+1)
        dijkstra(start,graph,distance)
        dist[start] = distance
            
    for i in range(1, n+1):
        answer = min (answer, dist[s][i] + dist[i][a] + dist[i][b])
    # 이때 ,s와 i가 같다면 -> a,b가 각각 택시에 탑승하는 것 (dist[s][s]는 0이므로)
    # s와 i가 다른 경우라면 -> s부터 i까지는 합승 + i부터 a로 , i부터 b로 가는 각각의 거리를 계산한다.
    return answer