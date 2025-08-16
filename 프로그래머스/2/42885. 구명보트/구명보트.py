def solution(people, limit):
    answer = 0
    people.sort()
    count = 0 # 최대 인원 수 
    weight = 0
    index = 0

    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer