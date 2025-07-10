def solution(n, m, section):
    answer = 0
    value = 0
    for i in range(len(section)):
        if section[i] <= value:
            continue
        if value >= section[-1] or value >= n: # 다 칠했다는 뜻 !
            break
        value = section[i] + m - 1 # value까지 칠해지는 것임
        answer += 1
    # 2 5 9 10
        
        
            
    return answer