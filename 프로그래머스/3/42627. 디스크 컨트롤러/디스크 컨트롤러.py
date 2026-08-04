import heapq
def solution(jobs):
    answer = 0
    i = 0
    q = []
    start, now = -1, 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now: # 얘는 시점을 가지고노는 변수라고 생각
                heapq.heappush(q, (j[1], j[0]))
        if q:
            take_time, now_time = heapq.heappop(q) # 소요시간 , 현재 시점
            start = now
            now = now + take_time
            answer = answer + (now - now_time)
            i += 1
            print(take_time, now ,now_time)
        else:
            now += 1 # 만약 처리할게 없다면 현재 처리시각을 1씩 늘리면서 검사를 시행한다
        
    return answer // len(jobs)