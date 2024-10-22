from collections import deque
def bfs(computers,visited,i):
    visited[i] = True
    
    queue = deque()
    queue.append(i)
    
    while queue:
        v = queue.popleft()
        for element in range(len(computers[v])):
            if not visited[element] and computers[v][element] == 1:
                queue.append(element)

                visited[element] = True 
def solution(n, computers):
    answer = 0

    visited = [False] * (n)
    
    for i in range(len(visited)):
        if visited[i] == False: # 만약 방문하지 않은 노드라면? 탐색 ㄱㄱ
            bfs(computers,visited,i)
            answer += 1

        
    return answer