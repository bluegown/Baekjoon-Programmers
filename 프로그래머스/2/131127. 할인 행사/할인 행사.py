def solution(want, number, discount):
    answer = 0
    
    dic = dict()
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
   

    for i in range(len(discount) - 9):
        dic2 = dict()
        arr = discount[i : i + 10]
        for j in range(10):
            dic2[arr[j]] = dic2.get(arr[j],0) + 1
            
        if dic == dic2:
            print(i)
            answer += 1
        
            
    return answer