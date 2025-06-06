def solution(answers):
    answer = []
    ans = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    score = [0,0,0]
    
    for index, value in enumerate(answers):
        if value == ans[0][index % len(ans[0])]:
            score[0] += 1
        if value == ans[1][index % len(ans[1])]:
            score[1] += 1
        if value == ans[2][index % len(ans[2])]:
            score[2] += 1
    
    for index, value in enumerate(score):
        if value == max(score):
            answer.append(index + 1)
    
    
    return answer