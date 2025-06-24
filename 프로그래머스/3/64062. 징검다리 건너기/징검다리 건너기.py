from copy import deepcopy
def jump(num , stones, k):
    skipRock = 0
    
    for stone in stones:
        if stone < num: # 건널 수 없음
            skipRock += 1
            if skipRock >= k:
                return False
        else:
            skipRock = 0 # 이어지지 않으니까 0으로 초기화해줌
    return True


def solution(stones, k):
    answer = 0
    
    start = 0
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        if jump(mid, stones, k) == False: # 이만큼 못건너요 줄여요
            end = mid - 1
        else:
            start = mid + 1 # 쌉가능 !
            answer = max(answer , mid)
            
            
        
        
        
            

    return answer