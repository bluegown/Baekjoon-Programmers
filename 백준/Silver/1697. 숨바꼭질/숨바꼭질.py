import sys
# sys.stdin.readline()
from collections import deque
sys.setrecursionlimit(100000000)
import heapq
INF = int(1e9)

def BFS(graph,start,dest):
    queue = deque()
    queue.append(start) # 시작점 원소부터 일단 큐 담는다.
    while queue:
        v = queue.popleft()
        if v == dest:
            print(graph[v])
            break

        for j in (v-1,v+1,2*v):
            if 0<=j<=100000 and not graph[j]: # 범위 사이에 존재하고, 겹치지 않는 원소라면
                graph[j] = graph[v] + 1
                queue.append(j)
            



N,K = map(int,sys.stdin.readline().split())
graph = [0] * 100001


BFS(graph,N,K)