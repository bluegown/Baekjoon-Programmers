def makeWord(ans , value, length):
    arr = ['A','E','I','O','U']
    if length == 6:
        return 
    if value != '':
        ans.append(value)
    for i in arr:
        makeWord(ans,''.join([value,i]),length + 1)
def solution(word):
    answer = 0
    ans = []
    makeWord(ans,'',0)
    return ans.index(word) + 1