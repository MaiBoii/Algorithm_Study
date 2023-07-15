#python3로는 시간초과라고 뜨는데 Pypy로는 됐다.

import sys
sys.setrecursionlimit(10000)

cnt = 0
n,v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

#방향이 없으므로 양방향으로 등록시킴
for _ in range(v):
    u,v = map(int,input().split())
    graph[u] += [v]
    graph[v] += [u]

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

for j in range(1,n+1):
    if visited[j] ==0:
        dfs(j)
        cnt += 1
print(cnt)
