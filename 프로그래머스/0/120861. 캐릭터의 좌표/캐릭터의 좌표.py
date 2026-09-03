def solution(keyinput, board):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # left , up , right , down 순서
    n = board[0] // 2
    m = board[1] // 2
    x,y = 0,0
    for i in keyinput:
        if i == "left":
            nx = x + dx[0]
            ny = y + dy[0]
        elif i == "up":
            nx = x + dx[1]
            ny = y + dy[1]
        elif i == 'right':
            nx = x + dx[2]
            ny = y + dy[2]
        else:
            nx = x + dx[3]
            ny = y + dy[3]
        if nx < -n or ny < -m or nx > n or ny > m:
            continue
        x = nx
        y = ny
        print(x,y)
    return [x,y]