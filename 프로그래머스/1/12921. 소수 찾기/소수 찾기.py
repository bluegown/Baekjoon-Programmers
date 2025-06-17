def isPrime(number):
    
    for i in range(2 , int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True # 소수인 경우
def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        if isPrime(i):
            answer += 1
            
    return answer