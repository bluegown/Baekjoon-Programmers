def solution(n, results):
    answer = 0
    graph = [['X' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    
    for x,y in results:
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = -1
    
     
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    for i in graph:
        if 'X' not in i:
            answer += 1
            
    return answer