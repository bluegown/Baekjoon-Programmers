def dfs(graph, visited, start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph , visited, i)
    
    return False
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                if j not in graph[i]:
                    graph[i].append(j)
                if i not in graph[j]:
                    graph[j].append(i)
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)
            answer += 1
                
    return answer