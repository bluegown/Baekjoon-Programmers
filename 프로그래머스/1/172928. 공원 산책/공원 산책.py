def chkoutIndex(nx , ny):
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return True
    return False
def solution(park, routes):
    answer = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i,j # 시작점 설정하기

    global N
    global M
    N = len(park)
    M = len(park[0]) 

    for i in routes:
        direction, move =  i.split()
        move = int(move)
        chk = True
        nx, ny = x , y
        if direction == 'E': # 동쪽
            ny = y + move
            if chkoutIndex(x, ny) == True:
                chk = False
                continue
            for j in range(y, ny + 1):
                if park[x][j] == 'X':
                    chk = False
                    break
        elif direction == 'S':
            nx = x + move
            if chkoutIndex(nx, y) == True:
                chk = False
                continue
            for j in range(x, nx + 1):
                if park[j][y] == 'X':
                    chk = False
                    break
        elif direction == 'W':
            ny = y - move
            if chkoutIndex(x, ny ) == True:
                chk = False
                continue
            for j in range(ny , y + 1):
                if park[x][j] == 'X':
                    chk = False
                    break
        else:
            nx = x - move
            if chkoutIndex(nx, y) == True:
                chk = False
                continue
            for j in range(nx, x + 1):
                if park[j][y] == 'X':
                    chk = False
                    break
        if chk == False:
            continue
        x = nx
        y = ny
    return [x,y]
            
        
    