def solution(answers):
    answer = []
    ans = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    value = []
    for i in range(len(ans)):
        count = 0
        for j in range(len(answers)):
            if i == 0:
                index = 5
            if i == 1:
                index = 8
            if i == 2:
                index = 10
            if answers[j] == ans[i][j % index]:
                count += 1
        value.append([i+1,count])
    value = sorted(value,key = lambda x: x[1], reverse = True)
    maxValue = -1
    print(value)
    for i in range(3):
        if value[i][1] >= maxValue:
            answer.append(value[i][0])
            maxValue = value[i][1]
    return answer