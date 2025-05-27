def solution(cards1, cards2, goal):
    answer = ''
    ans = []
    for i in range(len(goal)):
        if goal[i] in cards1:
            ans.append(cards1[0])
            cards1.pop(0)
        elif goal[i] in cards2:
            ans.append(cards2[0])
            cards2.pop(0)
            
    if goal == ans:
        answer = 'Yes'
    else:
        answer = 'No'

    return answer