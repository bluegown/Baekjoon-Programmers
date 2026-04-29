def solution(phone_book):
    answer = True
    
    set_pb = set(phone_book)
    
    for i in phone_book:
        st = ''
        for j in i:
            st += j
            if st != i and st in set_pb:
                return False # 본인과 같은 원소가 아니고, 현재까지 자른 string이 set()에 존재
        
    return answer