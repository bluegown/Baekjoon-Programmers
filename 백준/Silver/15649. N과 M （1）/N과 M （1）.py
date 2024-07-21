import sys
def dfs():
    if len(s) == M: # 만약 요구하는 길이가 다 된다면 
        print(' '.join(map(str,s)))
        return 
    for i in range(1,N+1):
        if visited[i]: # 만약 방문처리가 되어있다면
            continue
        visited[i] = True # 방문처리 후
        s.append(i) # 스택에 쌓아주고
        dfs()
        s.pop() #만약 끝나고 돌아왔다면, 이제 더이상 가지치기를 할 필요가 없으므로 pop
        visited[i] = False

N,M = map(int,sys.stdin.readline().split())

visited = [False] * (N+1)
s = []

dfs()

