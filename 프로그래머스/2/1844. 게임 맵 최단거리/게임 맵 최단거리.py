from collections import deque
def solution(maps):
    answer = 0
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # Maps[x][y] == 1인 경우만 통과가능
    queue = deque()
    queue.append((0,0))
    N = len(maps)
    M = len(maps[0])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maps[nx][ny] == 1: # 통행 가능한 경우
                queue.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
    if maps[N-1][M-1] <= 1:
        return -1
    return maps[N-1][M-1]