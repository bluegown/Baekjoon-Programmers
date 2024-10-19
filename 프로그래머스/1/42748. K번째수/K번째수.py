def solution(array, commands):
    answer = []
    
    for i in commands:
        ans = array[i[0]-1:i[1]]
        ans.sort()
        answer.append(ans[i[2]-1])



    return answer