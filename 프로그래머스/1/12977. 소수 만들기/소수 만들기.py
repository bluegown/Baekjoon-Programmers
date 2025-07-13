from itertools import combinations
def is_prime(num):
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            print(num)
            return True # 소수 아님 
    return False # 소수임
def solution(nums):
    answer = 0

    arr = list(combinations(nums, 3))
    
    for i in arr:
        if is_prime(i[0] + i[1] + i[2]) == False:
            answer += 1


    return answer