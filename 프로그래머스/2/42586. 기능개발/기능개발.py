


def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        period = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] !=0:
            period +=1
        answer.append(period) # 각각 걸리는 기간만큼을 넣어줌
    ans = []
    print(answer)

    count = 0
    elem = answer[0]
    while answer:
        v  = answer.pop(0) # 맨 아래꺼 꺼내고
        if v <= elem: # 만약 꺼낸게 v보다 크다면
                count +=1
        else:
                ans.append(count)
                elem = v
                count = 1 # 첫번째는 무조건이니깐
    ans.append(count)
        
        
    return ans
        