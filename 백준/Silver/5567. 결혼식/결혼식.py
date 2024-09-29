import sys

def bfs(graph,visited):
    global count
    q = []
    for i in graph[1]:
        q.append(i) 
        visited[i] = True
        count += 1

    while q:
        elem = q.pop()
        for i in graph[elem]:
            if visited[i] == False:
                count += 1
                visited[i] = True

    return count
    
    # 일단 자신의 친구를 q에 담아둔다



N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]


visited = [False] * (N+1)
visited[1] = True
count = 0
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs(graph,visited))