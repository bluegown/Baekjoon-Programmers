from collections import deque
def normalize(graph):
    min_x = min(x for x,y in graph)
    min_y = min(y for x,y in graph)
    result = []
    for x,y in graph:
        result.append((x - min_x , y - min_y))
    return sorted(result)
def rotate(shape):

    result = []

    for x, y in shape:
        result.append((y, -x))

    return normalize(result)

def bfs(graph , visited , i,j , target):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    
    arr = []
    arr.append((i,j))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if not visited[nx][ny] and graph[nx][ny] == target:
                queue.append((nx,ny))
                visited[nx][ny] = True
                arr.append((nx,ny))
    return arr
def solution(game_board, table):
    answer = 0
    visited = [[False] * len (game_board[0]) for _ in range(len(game_board))]
    queue = deque()
    game_board_dots = []
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and not visited[i][j]:
                game_board_dots.append(normalize(bfs(game_board, visited, i,j , 0)))
    visited = [[False] * len (table[0]) for _ in range(len(table))]
    table_dots = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1 and not visited[i][j]:
                table_dots.append(normalize(bfs(table, visited, i,j , 1)))
    
    used = [False] * len(table_dots)
    for blank in game_board_dots:
        for idx in range(len(table_dots)):
            if used[idx]: # 이미 사용한 블럭이면?
                continue
            piece = table_dots[idx]
            
            if len(blank) != len(piece):
                continue # 개수다르면 같을수 없지
            for _ in range(4):
                if blank == piece:
                    used[idx] = True
                    answer += len(blank) # 사용한 갯수만큼을 더해주고
                    break
                piece = rotate(piece)
            if used[idx]:
                break
    
    
    return answer