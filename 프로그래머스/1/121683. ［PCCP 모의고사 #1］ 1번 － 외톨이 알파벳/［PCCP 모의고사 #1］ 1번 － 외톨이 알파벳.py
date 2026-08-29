def solution(input_string):
    answer = []
    dic = dict()
    prev = input_string[0]
    dic[prev] = 1
    for i in range(1, len(input_string)):
        if prev == input_string[i]:
            continue
        dic[input_string[i]]  = dic.get(input_string[i],0) + 1
        prev = input_string[i]
    for key, value in dic.items():
        if value >= 2:
            answer.append(key)
    answer.sort()
    if len(answer) == 0:
        return 'N'
    return ''.join(answer)
            
        
        