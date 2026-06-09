def solution(n, results):
    answer = 0
    # n이 100 이하 > 플로이드 워셜 알고리즘 사용!
    
    graph = [['X' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0 # 대각선 원소는 0으로 초기화한다.
    for a,b in results:
        graph[a-1][b-1] = 1 # 승리
        graph[b-1][a-1] = -1 # 패배
    
    for k in range(n):
        for a in range(n): # A > K > B
            for b in range(n):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
                elif graph[a][k] == -1 and graph[k][b] == -1:
                    graph[a][b] = -1
    print(graph)
    for i in graph:
        if 'X' not in i:
            answer += 1
    return answer