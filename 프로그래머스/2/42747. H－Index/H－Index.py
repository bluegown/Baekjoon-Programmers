def solution(citations):
    answer = 0
    citations.sort()
    # 0 1 3 5 6 
    # 0번 이상 5개, 나머지 0번 이하
    # 1번 이상 4개, 나머지 1번
    # 3번 이상 3개, 나머지 2번
    # 5번 이상 2개, 나머지 3번
    for i in range(len(citations)):
        length = len(citations) - i
        if length <= citations[i]:
            return length  
    return 0