def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]

    maxX = 0
    maxY = 0
    for i in range(len(sizes)):
        if sizes[i][0] > maxX:
            maxX = sizes[i][0]
        if sizes[i][1] > maxY:
            maxY = sizes[i][1]
        
    return maxX * maxY