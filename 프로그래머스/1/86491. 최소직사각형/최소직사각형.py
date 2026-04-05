def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1], sizes[i][0]
    x = max(x[0] for x in sizes)
    y = max(x[1] for x in sizes)


    
                
                
    return x * y