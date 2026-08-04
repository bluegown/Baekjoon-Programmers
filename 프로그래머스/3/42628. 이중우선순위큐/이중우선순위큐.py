import heapq
def solution(operations):
    answer = []
    q = []
    for i in operations:
        op, num = i.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(q, num) # 최소힙
        if op == 'D' and num == -1:
            if q:
                heapq.heappop(q)
        if op == 'D' and num == 1:
            if q:
                q.remove(max(q))
                
            
    if q:
        return [max(q) , min(q)]
    else:
        return [0,0]