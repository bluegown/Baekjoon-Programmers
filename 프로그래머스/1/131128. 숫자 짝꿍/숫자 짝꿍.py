def solution(X, Y):
    answer = ''
    dic = dict()
    for i in range(len(Y)):
        if int(Y[i]) in dic:
            dic[int(Y[i])] += 1
        else:
            dic[int(Y[i])] = 1 # Y의 개수 카운팅
            
    ans = []
    for i in range(len(X)):
        if int(X[i]) in dic:
            if dic[int(X[i])] > 0: # 개수가 현재 존재하는 상태라면?
                ans.append(X[i])
                dic[int(X[i])] -= 1

    if len(ans) == 0:
        return "-1" # 짝궁존재 X
    else:
        if ans.count('0') == len(ans):
            return "0" # 짝궁이 오직 0으로만 구성되어있는 경우
        else:
            ans.sort(reverse = True)
        

    return ''.join(ans)