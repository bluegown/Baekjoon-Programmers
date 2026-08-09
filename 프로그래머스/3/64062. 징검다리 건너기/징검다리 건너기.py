def chkJump(stones, k, mid):
    skip_rock = 0
    
    for stone in stones:
        if stone < mid: # 여기로는 점프할 수 없는 경우
            skip_rock += 1
            if skip_rock >= k:
                return False # 점프 불가합니다 여긴..
        else:
            skip_rock = 0
    return True
        
        
            
        

def solution(stones, k):
    answer = 0
    start = 0
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        if chkJump(stones, k , mid): # 점프 뛸수 있으면? mid를 더 늘려봐
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
        
            
    return answer