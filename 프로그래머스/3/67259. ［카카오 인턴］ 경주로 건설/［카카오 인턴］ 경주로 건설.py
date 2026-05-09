from collections import deque
import copy
#직선 100원, 코너 500원 
def bfs(cost, board):
    queue = deque()
    queue.append((0,0,0))
    queue.append((0,0,2)) # 초기엔 동쪽, 남쪽만 갈수있으므로 2개만 넣어주고 시작
    for i in range(4):
        cost[0][0][i] = 0 # 초기엔 동서남북 모두 0임
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 동서남북에 맞춰 dx, dy 구성
    while queue:
        x,y, direction = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(board) or ny >= len(board[0]) or nx < 0 or ny < 0:
                continue # 조건 위배
            if board[nx][ny] == 1:
                continue # 도착할수 없는 노드
            if direction == i:
                new_cost = cost[x][y][direction] + 100 
            else:
                new_cost = cost[x][y][direction] + 600
                
            if new_cost < cost[nx][ny][i]:
                cost[nx][ny][i] = new_cost # 새로 갱신
                queue.append((nx,ny,i))
            
            
            
                
            
            
            
        
def solution(board):
    answer = 0
    dist = [[0] * (len(board[0])) for _ in range(len(board))]
    cost = [[[1e9 for _ in range(4)] for _ in range((len(board[0])))] for _ in range(len(board))]
    # 동서남북 0123으로 ㄱㄱ
    
    bfs(cost, board)
    return min(cost[-1][-1])