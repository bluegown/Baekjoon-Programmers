def solution(citations):
    citations.sort()

    for idx, value in enumerate(citations):
        if value >= len(citations) - idx:
            return len(citations) - idx
        
    return 0