def solution(today, terms, privacies):
    answer = []
    cnt = 0
    today = today.split('.')
    today = str(today[0]) + str(today[1]) + str(today[2])
    term = {}
    for i in terms:
        i = i.split()
        term[i[0]] = term.get(i[0],0) + int(i[1])
        
    for i in privacies:
        cnt += 1
        i = i.split()
        date, types = i[0], i[1]
        date = date.split('.')
        year , month , day = date[0],date[1],date[2]
        
        long = term[types] # 유효할 수 있는 최대 기간
        year = int(year) + (int(month) + int(long)) // 12
        if (int(month) + int(long)) % 12 == 0:
            year -= 1
        month = (int(month) + int(long)) % 12
        if month == 0:
            month = 12
        if month < 10:
            month = '0' + str(month)
        maxPrivacies =  str(year) + str(month) + day
        print(maxPrivacies , today)
        if maxPrivacies > today:
            continue
        else:
            answer.append(cnt)
        
        
        
    return answer