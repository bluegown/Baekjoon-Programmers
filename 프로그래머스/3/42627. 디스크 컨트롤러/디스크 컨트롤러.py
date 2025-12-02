import heapq
from collections import deque
def solution(jobs):
    answer = 0
    i = 0
    start = -1
    now = 0
    heap = []
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now: # 요청시점이 처리 가능하다면
                heapq.heappush(heap,[j[1],j[0]])
        if heap:
            l, s = heapq.heappop(heap) # l은 작업 소요시간 , s는 요청시점
            start = now
            now += l
            answer += (now - s)
            i += 1
        else:
            now += 1


    return answer // len(jobs)