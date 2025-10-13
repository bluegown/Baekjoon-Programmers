
def solution(tickets):
    answer = []
    
    graph = dict()
    for start,end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort(reverse = True)

    print(graph)
    stack = ["ICN"]
    while stack:
        top = stack[-1] # 왼쪽 원소부터 빼낸다
        if top in graph and graph[top]:
            stack.append(graph[top].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]