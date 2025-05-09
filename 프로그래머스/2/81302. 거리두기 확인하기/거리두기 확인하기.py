# 16:08 문제 읽기 시작
from collections import deque
import math
def solution(places):
    answer = [1] * len(places)
    
    for k in range(len(places)):
        graph = places[k]
        queue = deque()
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 'P':
                    queue.append((i,j)) # 큐에 모든 응시자들의 좌표를 담아둔다.

        
        while queue:
            x,y = queue.popleft() # 먼저 들어간 애부터 순차적으로 탐색한다
            for i in queue:
                if answer[k] == 0:
                    break
                x_value,y_value = i[0],i[1]
                if abs(x_value - x) + abs(y_value - y) > 2:
                    continue # 맨해튼 거리가 2 초과인 경우라면 넘어간다. 거리두기 준수중
                    
                else: # 만약 맨해튼 거리가 2 이하라면 (1또는 2) -> 파티션 유무 확인하기
                    if x_value == x and abs(y_value - y) == 1:
                        # print(x,y,x_value,y_value)
                        answer[k] = 0
                        break
                    if x_value == x and abs(y_value - y) == 2:
                        max_value = max(y,y_value)
                        if graph[x][max_value - 1] == 'X':
                            continue
                        else: # 둘의 거리가 2인데도 중간이 파티션이 아니라면?
                            answer[k] = 0
                            # print(x,y,x_value,y_value)
                            break
                    
                    if y_value == y and abs(x_value - x) == 1:
                        answer[k] = 0
                        # print(x,y,x_value,y_value)
                        break
                    
                    if y_value == y and abs(x_value - x) == 2:
                        max_value = max(x,x_value)
                        if graph[max_value - 1][y] == 'X':
                            continue
                        else: # 둘의 거리가 2인데도 중간이 파티션이 아니라면?
                            answer[k] = 0
                            # print(x,y,x_value,y_value)
                            break
        
                    if x_value != x and y_value != y: # 거리는 무조건 2로 고정
                        if x_value < x:
                            if graph[x][y_value] == 'X' and graph[x_value][y] == 'X':
                                continue
                            else:
                                # print(x,y,x_value,y_value)
                                answer[k] = 0
                        else:
                            if graph[x][y_value] == 'X' and graph[x_value][y] == 'X':
                                continue
                            else:
                                # print(x,y,x_value,y_value)
                                answer[k] = 0
        # print(answer)        
                        
                        
    
    return answer