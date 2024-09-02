def solution(nums):
    answer = 0
    arr = set(nums)
    maxlen = len(nums) // 2
    if maxlen == len(arr):
        return maxlen
    if maxlen < len(arr):
        return maxlen
    else:
        return len(arr)
    return maxlen