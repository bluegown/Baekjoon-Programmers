def solution(n, times):
    answer = 0
    times.sort()
    start = 1
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in times:
            total += (mid // i)
        if total >= n: # 모든 사람이 심사 가능함(필요 이상의 인원이 심사 가능한 경우)
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
            
    return answer