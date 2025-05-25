def makeWord(ans, value, length):
    if length == 6:
        return
    if value != '':
        ans.append(value)
    for i in ['A','E','I','O','U']:
        makeWord(ans, ''.join([value,i]), length + 1)
    
def solution(word):
    answer = 0
    ans = []
    makeWord(ans, '', 0) 
    return ans.index(word) + 1