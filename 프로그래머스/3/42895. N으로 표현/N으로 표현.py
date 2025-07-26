def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9): # N의 범위
        arr = dp[i] # 계산 횟수당 사용할 수 있는지를 검사하는 arr
        arr.add(int(str(N) * i)) # 555, 55와 같은 형태로 사용됨
        
        for j in range(1, i):
            for k in dp[j]: # 현재까지 계산해온 dp배열 내 기록된 수들에 대해서
                for m in dp[i - j]:
                    arr.add(k + m)
                    arr.add(k - m)
                    arr.add(k * m)
                    if k!= 0 and m!=0:
                        arr.add( k // m)
        
        if number in arr:
            return i
    
    return -1
                    