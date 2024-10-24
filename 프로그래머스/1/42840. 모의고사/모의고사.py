def solution(answers):
    answer = []
    
    ans = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    score = [0,0,0]
    for j in range(3): # 3명에 대해서 탐색 시작
        count = 0
        for k in range(len(answers)): #이제 안에있는 배열 구석구석 탐색 시작..
          if answers[k] == ans[j][k % len(ans[j])]:
            count += 1
        score[j] = count
                
        
    maxValue = max(score)
    for i in range(len(score)):
        if maxValue == score[i]:
            answer.append(i+1)
    return answer