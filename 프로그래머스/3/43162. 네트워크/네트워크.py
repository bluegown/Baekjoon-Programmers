def dfs(graph , visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph , visited, i)
    return 1

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, n+1):
            if computers[i-1][j-1] == 1 and i!= j:
                if j not in graph[i]:
                    graph[i].append(j)
                    graph[j].append(i)
    # dfs > stack
    visited = [False] * (n+1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            answer += dfs(graph , visited, start)

    return answer