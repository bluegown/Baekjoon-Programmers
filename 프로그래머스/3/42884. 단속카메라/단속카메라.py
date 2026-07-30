def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x:  x[1])
    cam = -30001
    for i in range(len(routes)):
        if routes[i][0] > cam:
            cam = routes[i][1]
            answer += 1
        
        
    return answer