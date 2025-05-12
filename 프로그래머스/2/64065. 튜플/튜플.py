def solution(s):
    answer = []
    x = []
    
    for i in range(1,len(s)):
        index = i
        count = 0
        if s[i] == '{':
            while True:
                if s[index] == '}':
                    break
                index += 1
            arr = s[i+1:index].split(',')
            x.append(arr)
            
    x = sorted(x, key = len)
    for i in range(len(x)):
        for j in range(len(x[i])):
            if int(x[i][j]) not in set(answer):
                answer.append(int(x[i][j]))
    


    return answer