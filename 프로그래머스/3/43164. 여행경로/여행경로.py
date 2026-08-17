        
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
        if top in graph and graph[top]: # graph[top]에 원소 존재 > 다음으로 갈 수 있는곳 존재
            stack.append(graph[top].pop())
        else: # 다음으로 갈 수 있는곳이 없네 이제..
            answer.append(stack.pop())
            
    return answer[::-1]
    