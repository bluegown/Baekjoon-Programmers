def solution(answers):
    answer = []
    ans = [[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5],[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0] * 3
    
    for i in range(len(ans)):
        for j in range(len(answers)):
            if answers[j] == ans[i][j % len(ans[i])]:
                score[i] += 1
    
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
        
    
    return answer