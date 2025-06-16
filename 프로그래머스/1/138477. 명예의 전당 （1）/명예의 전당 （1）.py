def solution(k, score):
    answer = []
    arr = []
    for i in score:
        if len(answer) < k:
            arr.append(i)
            arr.sort()
            answer.append(arr[0]) # arr append 하고 꼴찌 발표
        else:
            arr.append(i)
            arr.sort()
            answer.append(arr[-k])
            
    return answer