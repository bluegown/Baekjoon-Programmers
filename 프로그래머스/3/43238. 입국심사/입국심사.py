def solution(n, times):
    answer = 0
    times.sort() # O(NlogN)
    
    start = 1
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in times: 
            count += (mid // i)
        if count >= n: # 더 많은 사람을 받을 수 있음, 시간 줄이자
            result = mid
            end = mid - 1
        else:
            start = mid + 1

        
        
        
        
    return result