def solution(answers):
    answer = [0] * 3
    arr = [[1,2,3,4,5] , [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for index , value in enumerate(answers):
        if value == arr[0][index % len(arr[0])]:
            answer[0] += 1
        if value == arr[1][index % len(arr[1])]:
            answer[1] += 1
        if value == arr[2][index % len(arr[2])]:
            answer[2] += 1
        
    arr = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            arr.append(i + 1)
        
        
    return arr