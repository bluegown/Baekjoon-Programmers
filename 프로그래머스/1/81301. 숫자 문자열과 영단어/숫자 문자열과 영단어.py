def makeDict():
    dic = dict()
    dic["zero"] = 0
    dic["one"] = 1
    dic["two"] = 2
    dic["three"] = 3
    dic["four"] = 4
    dic["five"] = 5
    dic["six"] = 6
    dic["seven"] = 7
    dic["eight"] = 8
    dic["nine"] = 9
    
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