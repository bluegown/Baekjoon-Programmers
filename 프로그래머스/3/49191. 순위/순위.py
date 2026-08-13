def solution(n, results):
    answer = 0
    graph = [['X'] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
    for a,b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
                if graph[a][k] == -1 and graph[k][b] == -1:
                    graph[a][b] = -1
    for i in graph:
        if 'X' not in i:
            answer += 1
    return answer