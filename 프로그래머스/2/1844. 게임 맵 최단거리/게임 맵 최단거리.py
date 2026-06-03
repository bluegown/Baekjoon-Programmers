from collections import deque
def bfs(graph):
    queue = deque()
    queue.append((0,0)) # 초기 시작점 넣는다.
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
def solution(maps):
    answer = 0
    graph = maps
    bfs(graph)
    print(graph)
    if graph[-1][-1] == 1:
        return -1
    
    return graph[-1][-1]