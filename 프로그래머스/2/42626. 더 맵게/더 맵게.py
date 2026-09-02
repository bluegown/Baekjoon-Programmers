import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    tf = True
    while scoville:
        v = heapq.heappop(scoville)
        if v >= K: # 최솟값이 K보다 이제 크다면? 조건 충족
            tf = False
            break
        if scoville:
            heapq.heappush(scoville , v + (2 *  heapq.heappop(scoville)))
            answer += 1
    if tf:
        return -1
    
    return answer