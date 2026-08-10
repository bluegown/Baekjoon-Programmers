def solution(rows, columns, queries):
    answer = []
    
    graph = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1

    for i in queries:
        x1, y1, x2, y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        prev = graph[x1][y1]
        min_value = 10001
        for row in range(x1, x2):
            graph[row][y1] = graph[row + 1][y1] # 위쪽으로 옮기기
            min_value = min(min_value, graph[row][y1])
        for col in range(y1, y2):
            graph[x2][col] = graph[x2][col + 1] # 왼쪽으로 옮기기
            min_value = min(min_value, graph[x2][col])
        for row in range(x2, x1, -1): 
            graph[row][y2] = graph[row - 1][y2] # 아래로 옮기기
            min_value = min(min_value, graph[row][y2])
        for col in range(y2, y1 + 1, -1) :
            graph[x1][col] = graph[x1][col-1]
            min_value = min(min_value, graph[x1][col])
        graph[x1][y1 + 1] = prev
        min_value = min(min_value, prev)
        answer.append(min_value)
        
            
            
            
            
            
        
    
    return answer