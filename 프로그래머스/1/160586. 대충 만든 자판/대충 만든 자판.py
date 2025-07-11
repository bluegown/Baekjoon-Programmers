def solution(keymap, targets):
    answer = []
    keys = dict()
    
    for i in keymap:
        for j in range(len(i)):
            if i[j] in keys:
                keys[i[j]] = min(keys[i[j]], j) # 기존 인덱스랑 현재 인덱스의 비교
            else:
                keys[i[j]] = j # 만약 없다면

                
    
    for i in targets:
        count = 0
        for j in i: # target 내에있는 단어들에 대해 순회
            if j not in keys:
                count = -1
                break
            else: # 들어있다면 ?
                count += (keys[j] + 1)
        answer.append(count)    
    return answer