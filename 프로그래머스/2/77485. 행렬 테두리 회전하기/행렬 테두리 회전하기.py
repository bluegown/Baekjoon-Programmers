# 22:51 시작..오늘안에 풀이 가능하려나
import copy
def solution(rows, columns, queries):
    answer = []
    graph = []
    for i in range(rows):
        app = [i for i in range((i * columns) + 1, (i * columns) + columns + 1)]
        graph.append(app)
    
    for i in queries:
        
        x1,y1,x2,y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        min_value = graph[x1][y1]
        first_value = graph[x1][y1]
        # 왼쪽 위로 밀기
        for row in range(x1, x2):
            graph[row][y1] = graph[row + 1][y1]
            min_value = min(min_value , graph[row + 1][y1])
        # 아래 왼쪽으로 밀기
        for col in range(y1, y2):
            graph[x2][col] = graph[x2][col + 1]
            min_value = min(min_value , graph[x2][col + 1])
        for row in range(x2 , x1, -1):
            graph[row][y2] = graph[row-1][y2]
            min_value = min(min_value , graph[row-1][y2])
        for col in range(y2, y1 + 1, -1):
            graph[x1][col] = graph[x1][col - 1]
            min_value = min(min_value , graph[x1][col - 1])
        graph[x1][y1 + 1] = first_value
        answer.append(min_value)
    return answer