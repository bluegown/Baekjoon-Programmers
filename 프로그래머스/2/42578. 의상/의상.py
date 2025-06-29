def solution(clothes):
    answer = 1
    dic = dict()
    
    for item , category in clothes:
        dic[category] = dic.get(category,0) + 1

    for key, value in dic.items():
        answer = answer * (value + 1)

    
    return answer - 1