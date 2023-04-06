from collections import deque

#이동할 네 방향 정의
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return 

t = int(input())
for i in range(t):
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y]=1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt+=1
    print(cnt)