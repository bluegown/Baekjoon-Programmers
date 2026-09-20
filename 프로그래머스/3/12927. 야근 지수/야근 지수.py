import heapq
def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i] = -1 * works[i]
    heapq.heapify(works)
    i = 0
    while i < n:
        v = heapq.heappop(works)
        if v == 0:
            break
        v = v * (-1)
        v -= 1
        heapq.heappush(works, -v)
        i +=1
    for i in works:
        answer += i ** 2
    return answer