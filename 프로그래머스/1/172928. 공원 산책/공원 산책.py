def chkoutIndex(nx , ny):
    if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
        return True
    return False
def solution(park, routes):
    answer = []
    global rows #row 는 세로 
    global cols  #col은 가로
    rows = len(park)
    cols = len(park[0]) 
    for i in range(rows):
        for j in range(cols):
            if park[i][j] == 'S':
                row, col  = i,j # 시작점 설정하기



    for i in routes:
        direction, move =  i.split()
        move = int(move)
        chk = True
        next_row = row
        next_col = col
        if direction == 'E': # 동쪽
            next_col = col + move
            if chkoutIndex(row, next_col) == True:
                chk = False
                continue
            for j in range(col, next_col + 1):
                if park[row][j] == 'X':
                    chk = False
                    break
        elif direction == 'S':
            next_row = row + move
            if chkoutIndex(next_row, col) == True:
                chk = False
                continue
            for j in range(row, next_row + 1):
                if park[j][col] == 'X':
                    chk = False
                    break
        elif direction == 'W':
            next_col = col - move
            if chkoutIndex(row,next_col ) == True:
                chk = False
                continue
            for j in range(next_col , col + 1):
                if park[row][j] == 'X':
                    chk = False
                    break
        else:
            next_row = row - move
            if chkoutIndex(next_row, col) == True:
                chk = False
                continue
            for j in range(next_row, row + 1):
                if park[j][col] == 'X':
                    chk = False
                    break
        if chk == False:
            continue
        col = next_col
        row = next_row
    return [row,col]
            
        
    