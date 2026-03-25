def solution(nums):
    answer = 0
    
    num = len(nums) // 2 # max로 가질수 있는 숫자
    ans = set(nums)
    if len(ans) <= num:
        return len(ans)
    else:
        return len(nums) // 2
    



    return answer