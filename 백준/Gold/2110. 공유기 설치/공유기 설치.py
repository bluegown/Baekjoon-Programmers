import sys
# sys.stdin.readline()
from collections import deque
sys.setrecursionlimit(100000000)
import heapq
import copy
import itertools
from itertools import combinations
from itertools import permutations
INF = 1e9
from bisect import bisect_left,bisect_right

N,C = map(int,sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))
array.sort()
end = array[-1] - array[0] 
start = 1
while start <= end:
    count = 1
    mid = (start + end) // 2
    current = array[0]
    for i in range(1,len(array)):
        if array[i] - current >= mid:
            count +=1
            current = array[i]
    if count >= C: # 공유기가 더 설치되거나 딱 맞게 설치되는 경우, 범위를 넓혀야 한다 
        start = mid + 1 # 범위를 넓혀야 하는 거니까 mid를 더 넓혀야 적게 설치
        answer = mid
    else: # 공유기가 덜 설치된 경우, 범위를 좁혀야 한다
        end = mid - 1 # end를 줄이는 방법으로 mid를 더 좁혀야 많이 설치
print(answer)