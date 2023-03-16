import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph,v,visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    #연결된 노드 방문
    for i in graph[v]:
        #방문하지 않은 노드의 경우
        if not visited[i]:
            cnt += 1
            dfs(graph,i,visited)

dfs(graph,r,visited)

for i in range(1, n+1):
    if visited[i] != 0:
        print(visited[i])
    else:
        print(0)