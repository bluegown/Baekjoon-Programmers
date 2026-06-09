def solution(n, costs):
    answer = 0
    costs = sorted(costs, key = lambda x:x[2])
    parents = [i for i in range(n)]
    
    def find_parent(parents, x):
        
        if parents[x] != x:
            parents[x] = find_parent(parents, parents[x]) # 부모 찾아 돌려돌려
        return parents[x]
    def union(parents,x, y):
        x = find_parent(parents, x)
        y = find_parent(parents, y)
         
        if x < y:
            parents[y] = x
        else:
            parents[x] = y
    for a,b,cost in costs:
        if find_parent(parents, a) != find_parent(parents, b):
            answer += cost
            union(parents, a, b)
    return answer