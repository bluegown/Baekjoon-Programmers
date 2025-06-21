def binary_search(n , times):
    start = 1
    times.sort()
    end = times[-1] * n # 시간이 기준이 된다!!
    
    
    while start <= end:
        mid = (start + end) // 2 
        count = 0
        for i in times:
            count += (mid // i) # 인당 평가할 수 있는 시간 
        if count < n: # 모든 사람 평가하지 못하는 경우
            start = mid + 1
        else: # 여유롭게 평가 가능함
            end = mid - 1
            ans = mid
        
    return ans   

def solution(n, times):
    answer = 0
    
    return binary_search(n,times)