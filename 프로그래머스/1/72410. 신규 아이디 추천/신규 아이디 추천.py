def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    # 1단계 문제 없음 
    
    second_id = []
    for i in range(len(new_id)):
        if 'a' <= new_id[i] <='z' or new_id[i] in {'-','_','.'} or '0' <= new_id[i] <= '9': # 문자 충족한 경우
            second_id.append(new_id[i])
        else: # 제거
            continue
    second_id = ''.join(second_id)
    
    while '..' in second_id: #3단계
        second_id = second_id.replace('..','.') # 연속된 마침표가 전부 치환될때까지 진행
        

    second_id = second_id.strip('.')
    
    second_id = list(second_id) 
    
    if len(second_id) == 0: # 5단계
        second_id.append('a') 
        
    if len(second_id) >= 16: # 6단계
        second_id = second_id[0:15] # 0~ 14까지 생존
        if second_id[-1] == '.':
            second_id.pop()
        
    value = second_id[-1]
    if len(second_id) <= 2: # 7단계
        while len(second_id) < 3:
            second_id.append(value)
    
        
    
    return ''.join(second_id)