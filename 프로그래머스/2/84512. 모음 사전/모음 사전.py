def make_word(now, ans):
    if len(now) == 5:
        return False
    arr = ['A','E','I','O','U']
    for i in arr:
        ans.append(now + i)
        make_word(now + i, ans)
    
        
def solution(word):
    answer = []
    arr = ['A','E','I','O','U']
    for i in arr:
        answer.append(i)
        make_word(i, answer)
    return answer.index(word) + 1