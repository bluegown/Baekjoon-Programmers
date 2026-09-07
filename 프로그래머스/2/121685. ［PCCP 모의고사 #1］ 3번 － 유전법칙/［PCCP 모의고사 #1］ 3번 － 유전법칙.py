def find_parent(gen, index):
    if gen == 1:
        return 'Rr' # 1세대는 Rr로 고정인듯 하네
    # 만약 (3,5)를 찾고싶다면.. 
    # (3,5) -> (2,1) -> (1,0)
    
    parent = find_parent(gen -1 , (index - 1) // 4 + 1)
    if parent == 'RR' or parent == 'rr':
        return parent
    if index % 4 == 1:
        return 'RR'
    elif index % 4 == 0:
        return 'rr'
    else:
        return 'Rr'
    # 아니면 부모가 'Rr' 이라는 소리니까.
        
        # 여기서는 'RR' 아니면 'rr'
def solution(queries):
    answer = []
    # 4^(n-1)에 16승 하면 무조건 터진다. 절대 완전한 모든것을 만들수 없음
    for n,p in queries:
        answer.append(find_parent(n,p))
    return answer