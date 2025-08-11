def change(n):
    arr = []
    while n > 0:
        arr.append(n % 2)
        n = n // 2
            
    return arr[::-1]
        
def solution(n):
    answer = 0
    ans = change(n)
    num = ans.count(1)
    for i in range( n + 1, 1000001):
        arr = change(i)
        if num == arr.count(1):
            return i
        
    return answer