def solution(n):
    answer = 0
    
    dp = [0] * (n+1)
    
    if n == 1 or n == 2:
        return n

    dp[1] = 1 # 제자리에서 1칸 점프
    dp[2] = 2 # 1칸 1칸, 2칸 
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    print(dp)    
    return dp[n]