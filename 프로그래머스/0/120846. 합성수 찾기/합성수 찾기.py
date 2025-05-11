def solution(n):
    answer = 0
    
    for i in range(1,n+1): # 이래야 1부터 n까지 돌아가지
        for j in range(2, int(i ** (0.5)) + 1):
            if i % j == 0:
                answer += 1 
                break

        
    return answer