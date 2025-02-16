def solution(name, yearning, photo):
    answer = []
    
    dictarr = {}
    
    for i in range(len(name)):
        dictarr[name[i]] = yearning[i]
    
    for i in photo: # photo의 길이만큼 돌아감
        sum = 0
        for j in i: # photo[i]의 길이만큼 돌아감. 모든 원소의 검사
            if j in dictarr:
                sum += dictarr[j]
        answer.append(sum)
    return answer