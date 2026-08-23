from collections import deque
def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    
    cost = [[[1e9 for _ in range(4)] for _ in range((len(board[0])))] for _ in range(len(board))]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append((0,0,1)) # x,y좌표 + 동쪽
    queue.append((0,0,2)) # x,y좌표 + 남쪽

    for i in range(4):
        cost[0][0][i] = 0
    # 서, 남, 동, 북 순서로 가네
    while queue:
        x,y, direction = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>= n or ny >= m:
                continue
            if board[nx][ny] == 1:
                continue # 벽 설치로 인해 설치 불가
                
            if i == direction:
                costs = cost[x][y][direction] + 100
            else:
                costs = cost[x][y][direction] + 600
                
            if costs < cost[nx][ny][i]:
                cost[nx][ny][i] = costs
                queue.append((nx,ny,i))
    return min(cost[n-1][m-1])