def solution(n):
    answer = 0
    
    for i in range(1,n+1): # i는 시작하는 인덱스고
        sumValue = 0
        for j in range(i, n+1): # j는 간격이지
            sumValue += j # 이렇게 하면 i부터 천천히 시작
            if sumValue == n: 
                answer += 1
            elif sumValue > n:
                break
            
    return answer