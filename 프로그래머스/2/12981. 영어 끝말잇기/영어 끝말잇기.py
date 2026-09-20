def solution(n, words):
    answer = []
    arr = set()
    last_word = words[0]
    arr.add(words[0])
    for i in range(1,len(words)):
        if words[i] not in arr:

            if last_word[-1] != words[i][0]: # 이경우도 탈락. 마지막 말이랑 첫말이랑 다른 경우
                return [ (i % n) + 1, i  //n  + 1]
            else:
                arr.add(words[i])
        else: # 만약 말한 단어를 또 말하는 경우 > 탈락
            return [ (i % n) + 1, i //n  + 1]
        last_word = words[i]
# [탈락하는 사람 번호 및 몇번째 차례인지]
    return [0,0]