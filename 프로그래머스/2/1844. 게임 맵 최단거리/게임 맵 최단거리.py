from collections import deque
def solution(maps):
    answer = 0
    
    queue = deque()
    queue.append((0,0))
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    graph = [[0] * len(maps[0]) for _ in range(len(maps))]
    n , m = len(maps) , len(maps[0])
    graph[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1 and graph[nx][ny] == 0: # 방문 가능한 곳이고 아직 미방문인 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
            
    if graph[n-1][m-1] == 0:
        return -1
    return graph[n-1][m-1]