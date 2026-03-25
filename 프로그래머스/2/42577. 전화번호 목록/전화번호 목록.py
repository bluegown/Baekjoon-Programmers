def solution(phone_book):
    answer = True
    
    s = set(phone_book)
    
    for i in phone_book:
        string = ''
        for j in i:
            string += j
            if string in s and string!=i:
                return False
            
    
    return answer