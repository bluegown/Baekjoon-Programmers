def solution(n, times):
    answer = 0
    times.sort()
    start = 0 
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in times:
            count += (mid // i)
        if count >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    

        
        
        
        
    return answer