import heapq
def solution(jobs):
    answer = 0
    start, now = -1, 0
    count = 0
    q = []
    while count < len(jobs):
        for j in range(len(jobs)):
            if start < jobs[j][0] <= now:
                heapq.heappush(q,(jobs[j][1], jobs[j][0])) # 처리대상에 넣고
        # 한바퀴를 다 돌았다.
        # 우선순위가 될거를 앞에다가 놔주면 된다
        if q:
            take_time, start_time = heapq.heappop(q) # 처리 대상 시작시간 / 처리 소요시간
            start = now # 처리할 원소를 최신화해준다
            now += take_time
            answer += (now - start_time)
            count += 1
        else:
            now += 1
            
                
        
        
    return answer // len(jobs)