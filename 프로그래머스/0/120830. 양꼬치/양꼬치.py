def solution(n, k):
    answer = 0
    if n >= 10:
        k -= (n // 10) # 음료수 개수 빼기
        
    answer = 12000 * n + 2000 * k 
    return answer