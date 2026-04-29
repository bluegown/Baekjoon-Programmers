def solution(nums):
    answer = 0
    arr = dict()
    for i in nums:
        arr[i] = arr.get(i,0) + 1
    print(arr)
    if len(arr) == len(nums) // 2: # 딱 N / 2개의 종류가 있는 경우
        return len(arr)
    elif len(arr) > len(nums) // 2: # 4마리 포켓몬이 있는데 3가지 종류 가지고있는 경우
        return len(nums) // 2
    else:
        return len(arr)
    return answer