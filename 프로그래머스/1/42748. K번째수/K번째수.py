def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = array [i - 1 : j ] # i ~ j까지 자르기
        arr.sort()
        answer.append(arr[k - 1])
    return answer