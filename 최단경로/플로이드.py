import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

#2차원 리스트 
graph = [[INF] * (n+1) for _ in range(n+1)]

#본인에게 가는 비용은 0 (대각선)
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
#각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    #A에서 B로 가는 비용은 C
    a,b,c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 거 출력하기
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
        