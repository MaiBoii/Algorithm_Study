#해당 문제는 BFS로 쉽게 풀 수 있다!
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

#이동할 네 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS 소스코드 구현
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 계속
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문할 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # print()
    # for i in graph:
    #     for j in i:
    #         print(j, end='')
    #     print()
                 
    return graph[N-1][M-1]

print(bfs(0,0))



