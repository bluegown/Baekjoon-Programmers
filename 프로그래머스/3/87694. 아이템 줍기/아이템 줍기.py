from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 102 for _ in range(102)] # - 1은 외부
    distance = [[0] * 102 for _ in range(102)] 
    visited = [[False] * 102 for _ in range(102)] # - 1은 외부
    for left_x, left_y, right_x, right_y in rectangle:
        left_x,left_y,right_x,right_y = left_x * 2, left_y * 2, right_x * 2, right_y * 2
        for i in range(left_x , right_x + 1):
            for j in range(left_y, right_y + 1):
                if left_x < i < right_x and left_y < j < right_y:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    queue = deque()
    queue.append((characterX * 2, characterY * 2))
    visited[characterX * 2][characterY * 2] = True
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
                return distance[x][y] // 2
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
 
        
    return distance[itemX][itemY] // 2