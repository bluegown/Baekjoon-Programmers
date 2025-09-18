import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    num = -1
    while scoville:
        value = heapq.heappop(scoville) # 가장 작은 원소 뺀다
        if value >= K: # 모든 스코빌 지수가 K보다 이상인 경우
            num = answer
            break
        answer += 1  # 뺀 횟수
        if len(scoville) == 0:
            break
        heapq.heappush(scoville, value + (heapq.heappop(scoville) * 2))
            
    
    
    
    return num