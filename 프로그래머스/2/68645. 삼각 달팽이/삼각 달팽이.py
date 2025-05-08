def solution(n):
    answer = []
    graph = [[0] * i for i in range(1,n+1)]
    move_types = ['down','right','up']
    index = 1
    row,col = n-1,n-1
    sum_value= (n * (n+1)) // 2

    for rows in range(n):
        
        graph[rows][0] = index
        index += 1 
    for cols in range(1,n):
        
        graph[n-1][cols] = index
        index += 1

    

    
    while True:
        if index > sum_value:
            break
        for i in range(1,n): # 대각선 왼쪽 올라가기, 현재 인덱스는 할필요 없음
            if row - i < 0 or col - i < 0:
                break # 더이상 탐색할필요 x . 인덱스 아웃
            if graph[row-i][col-i] != 0 or row - i<0 or col - i< 0: # 0,0이 이미 갱신된적이 있는거면 1,1이 막
                row = row - i + 1
                col = col - i + 1
                break
            graph[row-i][col-i] = index
            index += 1
            
            
        for i in range(row + 1,n): # 현재 row부터 n행까지 내려간다
            if graph[i][col] != 0 or i >= n:
                row = i - 1
                break # 이미 갱신된 점을 지나가서는 안된다.
            graph[i][col] = index
            index += 1
            
            
        for j in range(col + 1,row + 1): # col + 1 부터 끝까지 (우측이동)
            if graph[row][j] != 0:
                col = j - 1
                break
            graph[row][j] = index
            index += 1
        
            
    for i in graph:
        for j in i:
            answer.append(j)
            
        
            
            
        
        
    
    
    
    
    
    return answer