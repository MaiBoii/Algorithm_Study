'''
n = 도시 개수
m = 도로 개수
k = 거리 정보
x = 출발 도시 번호
'''

n,m,k,x = map(int, input().split())
city_map = [[] for _ in range(n+1)]
visited = [0]*(n+1)
distance = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    city_map[a] += [b]


def dfs(v):
    visited[v]=1
    cnt = 0
    for i in city_map[v]:
        if visited[i] == 0:
            cnt += 1
            distance[i]
            dfs(i)

print(city_map)