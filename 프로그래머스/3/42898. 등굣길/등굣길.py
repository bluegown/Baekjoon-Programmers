from collections import deque
def solution(m, n, puddles):
    answer = 0

    arr = [[0] * (m) for i in range(n)]
    arr[0][0] = 1

    
    for x in range(m):
        for y in range(n):
                if [x + 1, y + 1] in puddles:
                    continue
                if x == 0 and y == 0:
                    continue
                arr[y][x] = (arr[y-1][x] + arr[y][x-1]) % 1000000007 # 다른곳에서도 오는 

    
    
    
            
            
    return arr[-1][-1] 