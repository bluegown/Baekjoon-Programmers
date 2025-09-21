from collections import deque
def solution(n, results):
    answer = 0
    
    graph = [['X' for _ in range(n)] for i in range(n)]
    
    for i in range(n):
        graph[i][i] = 0 # 자기 자신
        
    for i in results:
        graph[i[0] - 1][i[1] - 1] = 1 # 승
        graph[i[1] - 1][i[0] - 1] = -1 # 패 
        
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = - 1
    print(graph)             
    for i in graph:
        if 'X' not in i:
            answer += 1
    
        
        
        
    
        
            
        
        
    return answer