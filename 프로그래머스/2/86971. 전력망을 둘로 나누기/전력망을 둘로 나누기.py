# 10:54 풀이 시작
from collections import deque
import copy
def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n+1)
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        # a를 돌려보고 , b는 n에서 빼면 나오네
        graph_test = copy.deepcopy(graph)
        graph_test[a].remove(b)
        graph_test[b].remove(a)
        visited = [False] * (n+1)
        
        queue = deque()
        queue.append(a) # 1번부터 탐색 시작하자
        
        visited[a] = True
        count = 1
        while queue:
            v = queue.popleft() # 원소 꺼내서 bfs 시작한다
            for i in graph_test[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    count += 1
        answer = min (answer, abs(n - (2 * count)))
        
    
    return answer