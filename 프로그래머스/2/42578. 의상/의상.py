def solution(clothes):
    answer = 1
    ans = dict()
    for key, value in clothes:
        ans[value] = ans.get(value,0) + 1
    for key, value in ans.items():
        answer = answer * (value + 1)
    return answer - 1