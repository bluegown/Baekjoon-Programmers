from itertools import combinations

def isPrime(num):
    for i in range(2, int(num ** (0.5) + 1)):
        if num % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    arr = list(combinations(nums , 3)) # 3개 원소 선별하고 
    
    for i in arr:
        
        if isPrime(int(i[0] + i[1] + i[2])) == True:
            answer += 1
            

    return answer