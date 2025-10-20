from collections import deque
def bfs(computers, visited , start):
    if visited[start] == True:
        return 0 # false면 순회돌 필요 없지
    visited[start] = True
    queue = deque()
    queue.append(start)
    
    while queue:
        elem = queue.popleft()
        for i in range(len(computers)):
            if visited[i] == False:
                if start!= i and computers[elem][i] == 1:
                    queue.append(i)
                    visited[i] = True    
    return True
def solution(n, computers):
    answer = 0
    visited = [False]  * (n)
    # 1번부터 시작해서 visited가 false면 돌려돌려
    
    for i in range(n):
        if bfs(computers,visited,i) == True:
            answer += 1
        
    return answer