# 23:10 풀이 시작
def find(gen, srno):
    if gen == 1:
        return 'Rr' # 1세대라면 Rr 반환
    
    parent = find(gen - 1, (srno - 1) // 4 + 1) # 부모를 찾는다! 9~ 13이면 3번째가 부모임.
    if parent == 'RR' or parent == 'rr':
        return parent # 부모가 이거면 나머지도 전부 같기에 더이상 호출할 필요가 없음
    # 그 아래까지 내려왔다면 'Rr'인 경우
    if srno % 4 == 1:
        return 'RR'
    elif srno % 4 == 0:
        return 'rr'
    else:
        return 'Rr'
    
    
def solution(queries):
    answer = []
    for n,p in queries:
        answer.append(find(n,p))
            
            
    return answer