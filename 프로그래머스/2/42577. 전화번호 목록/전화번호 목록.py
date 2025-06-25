def solution(phone_book):
    answer = True
    book_dict = set()
    for i in phone_book:
        book_dict.add(i)
    
    for i in phone_book:
        string = ''
        for j in i:
            string += j
            if string in book_dict and string!=i: # 접두어인 경우, 완전같으면 안됨
                return False

    
    
    
    return True