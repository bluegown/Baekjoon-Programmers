def solution(new_id):
    answer = ''
    
    new_id = new_id.lower() # 1단계
    print("1단계 " + new_id)
    
    new_id2 = []
    for i in new_id:
        if i.isalpha() or i in {'-','_','.'} or i.isdigit():
            new_id2.append(i)
    new_id2 = ''.join(new_id2)
    print("2단계 " + new_id2)
    
    while '..' in new_id2:
        new_id2 = new_id2.replace('..','.')
    
    print("3단계 " + new_id2)
    
    new_id2 = new_id2.strip('.')
    print("4단계 " + new_id2)
    if len(new_id2) == 0:
        new_id2 += 'a'
    print("5단계 " + new_id2)
    
    if len(new_id2) >= 16:
        new_id2 = new_id2[0:15]
        new_id2 = new_id2.strip('.')
    print("6단계 " + new_id2)
    # 0자라면 3번, 1자라면 2번, 2자라면 1번
    if len(new_id2) <= 2:
        string = new_id2[-1] * (3 - len(new_id2))
        new_id2 += string
    print("7단계 " + new_id2)
        
        
    
    
    
    return new_id2