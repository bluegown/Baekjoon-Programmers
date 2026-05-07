def solution(s):
    answer = ''
    dic = {"zero" : 0 , "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, 
          "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    string = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            string += s[i] # 하나씩 쌓아간다
        if string in dic:
            answer += str(dic[string])
            string = ''
    
            
    return int(answer)