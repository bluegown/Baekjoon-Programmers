def solution(phone_book):
    answer = True
    phone = set(phone_book)
    
    for i in phone_book:
        string = ''
        for j in i:
            string += j # 한글자씩 더해본다
            if string!= i and string in phone: # 만약 포함되어있다면?
                return False
        
    return True