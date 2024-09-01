import copy
def solution(arr):
    answer = []
    count = 0 
    for i in range(len(arr)):
        answer.append(arr[i])
        if [arr[i]] == arr[i+1:i+2]:
            answer.pop()
            
    
    return answer
            
