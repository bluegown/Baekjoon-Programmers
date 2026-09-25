from collections import deque
def solution(maps):
    answer = 0
    queue = deque()
    queue.append((0,0))
    n, m = len(maps), len(maps[0])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0: # 방문 불가능한 노드
                continue
            if not visited[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx,ny))
            
    if not visited[-1][-1]:
        return -1
    return maps[-1][-1]
