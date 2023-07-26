from collections import deque

n,m = map(int,input().split())
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))

visited = [[-1] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    visited[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if area[nx][ny] == 0:
                    visited[nx][ny] = 0 
                elif area[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if area[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
