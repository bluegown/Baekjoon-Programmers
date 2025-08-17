def solution(k, tangerine):
    answer = 0
    # 조합은 100000C50000 을 생각해보면 ,, 절대 안 될 것 같다...
    # O(N)으로 처리할 방법을 생각해보자
    x = [0] * 10000001
    arr = []
    for i in tangerine:
        x[i] += 1
    for index, value in enumerate(x):
        if value != 0:
            arr.append((index, value))
            
        
    arr = sorted(arr, key = lambda x: x[1],reverse = True)
    sumValue = 0
    count = 0
    for i in arr:
        sumValue += i[1]
        count += 1
        if sumValue >= k:
            break
    return count
