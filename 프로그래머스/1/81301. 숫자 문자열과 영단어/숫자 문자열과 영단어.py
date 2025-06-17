def makeDict():
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    return dic
def solution(s):
    answer = ""
    string = ""
    
    dic = makeDict()
    
    for i in range(len(s)):
        string += s[i]
        if string in dic:
            answer += str(dic[string])
            string = ""
        elif string.isdigit():
            answer += string
            string = ""
            
        
    return int(answer)