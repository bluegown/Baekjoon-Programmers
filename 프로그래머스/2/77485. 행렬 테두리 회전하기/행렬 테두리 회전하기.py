# 19:28 문제 읽기 시작
import copy
def turn(graph,x1,y1,x2,y2):
    first_value = graph[x1][y1]
    min_value = first_value
    for row in range(x1,x2): # 
        graph[row][y1] = graph[row+1][y1]
        min_value = min(min_value,graph[row+1][y1])
    
    for col in range(y1,y2):
        graph[x2][col] = graph[x2][col + 1]
        min_value = min(min_value,graph[x2][col+1])
        
    for row in range(x2,x1,-1):
        graph[row][y2] = graph[row-1][y2]
        min_value = min(min_value,graph[row-1][y2])
    
    for col in range(y2, y1 + 1, -1):
        graph[x1][col] = graph[x1][col -1]
        min_value = min(min_value,graph[x1][col-1])
        
    graph[x1][y1+ 1] = first_value

    
    return min_value            

        
    
def solution(rows, columns, queries):
    answer = []
    global ans
    graph = [[0] * columns for _ in range(rows)]
    index = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = index
            index += 1
    
    for i in queries:
        x1, y1, x2, y2 = i[0]- 1, i[1]- 1, i[2]-1 , i[3] -1
        answer.append(turn(graph,x1,y1,x2,y2))
        
    return answer