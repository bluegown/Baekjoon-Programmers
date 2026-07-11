def solution(park, routes):
    answer = []
    # 1. 주어진 방향으로 이동시 공원을 벗어나는지
    # 2. 이동 중 장애물을 만나는지 확인
    graph = [[] for _ in range(len(park))]
    for i in range(len(park)):
        for j in range(len(park[0])):
            graph[i].append(park[i][j])
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'S':
                x,y = i,j # 시작점 세팅
    # N, S , W, E (세로, 가로)
    # 북쪽으로 한칸. 세로 한칸 차감
    # 남쪽으로 한칸, 세로 한칸 추가
    # 서쪽으로 한칸, 가로 한칸 차감
    # 동쪽으로 한칸, 가로 한칸 추가
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # S, N, E, W
    # 1. 벽 검사
    # 2. 장애물 검사
    N = len(graph)
    M = len(graph[0])
    way = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
    for i in routes:
        dr, cnt = i.split()
        flag = False
        nx = x + dx[way[dr]] * int(cnt)
        ny = y + dy[way[dr]] * int(cnt)
        if nx >= N or ny >= M or nx < 0 or ny < 0:
            continue
        nx,ny = x,y
        for _ in range(int(cnt)):
            nx = nx + dx[way[dr]]
            ny = ny + dy[way[dr]]
            print(nx,ny , graph[nx][ny], way[dr])
            if graph[nx][ny] == 'X':
                flag = True
                break
        if flag:
            continue
        x,y = nx,ny
    return [x,y]