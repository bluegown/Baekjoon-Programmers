from collections import deque
def solution(maps):
    answer = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append((0,0))
    ans = [[-1 for _ in range(M)] for _ in range(N)]
    ans[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if ans[nx][ny] == -1 and maps[nx][ny] == 1:
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx,ny))
        maps[x][y] = 0

            
        
        
    
    return ans[N-1][M-1]