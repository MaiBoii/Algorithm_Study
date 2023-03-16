import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph,v,visited):
    global cnt
    queue = deque([r])
    #현재 노드를 방문 처리
    visited[r] = 1
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

bfs(graph,r,visited)

for i in range(1,n+1):
    if visited[i] != 0:
        print(visited[i])
    else:
        print(0)