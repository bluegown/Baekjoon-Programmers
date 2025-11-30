def solution(skill, skill_trees):
    answer = 0
    
    for arr in skill_trees:
        count = 0
        for i in range(len(arr)):
            if arr[i] in skill:
                if skill[count] == arr[i]: # 선행대로 진행
                    count += 1
                else:
                    count = -1
                    break
        if count!= -1:
            answer += 1
                
            
    return answer