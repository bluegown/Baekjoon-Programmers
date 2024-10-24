def solution(brown, yellow):
    answer = []
    y = []
    for i in range(1, int((yellow)**(1/2)) + 1):
        if yellow % i == 0: # 만약 i로 나누어 떨어진다면 ?
            y.append([i,yellow // i])
            
    total = []
    for i in range(1, int((brown + yellow)**(1/2)) + 1):
        if (brown + yellow) % i == 0: # 만약 i로 나누어 떨어진다면 ?
            total.append([i,(yellow + brown) // i])
    
    for i in total:
        for j in y:
          if (i[0]-2 == j[0] and i[1] - 2 == j[1]):
            return [i[1],i[0]]
          if (i[1]-2 == j[0] and i[0] -2 == j[1]):
            return [i[0],i[1]]
