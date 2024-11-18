import sys
# sys.stdin.readline()
import heapq
import copy
import itertools
from itertools import combinations
from itertools import permutations
from collections import deque
import math
sys.setrecursionlimit(100000000)
INF = 1e9
    
N,K = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,N+1)]

count = 0
result = []
index = 0

for _ in range(N):
    index += K-1
    if index >= len(arr):
        index %= len(arr)
    result.append(str(arr[index]))
    arr.pop(index)
print("<",", ".join(result)[:],">", sep='')