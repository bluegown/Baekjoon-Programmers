import sys
from collections import deque

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >=N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0

        
        

T = int(input())

for _ in range(T):
    answer = 0
    M,N,K = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(K):
        a,b = map(int,sys.stdin.readline().split())
        graph[a][b] = 1
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                answer += 1
                
    print(answer)
        

    
        