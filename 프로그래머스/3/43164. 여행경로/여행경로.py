from collections import deque
def solution(tickets):
    answer = []
    graph = dict()
    for a,b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    for key, value in graph.items():
        graph[key].sort(reverse = True)
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top in graph and graph[top]: # 다음으로 갈 원소가 있는 경우
            stack.append(graph[top].pop())
        else: # 이제 갈곳이 없다.. 순회가 끝난 경우라면?
            answer.append(stack.pop())# 마지막에 거꾸로 담고
            
            
            
        
    return answer[::-1] # 다시 이걸 거꾸로 담는 행위이다.