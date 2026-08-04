import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        v = heapq.heappop(scoville)
        if v >= K:
            return answer
        
        if scoville:
            heapq.heappush(scoville, v + heapq.heappop(scoville) * 2)
            answer += 1
    return -1