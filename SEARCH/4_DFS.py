#인접 행렬(Adjacency Matrix) : 2차원 배열 방식으로 그래프 표현
INF = 99999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5,INF,0]
]

print(graph)

#인접 리스트(Adjacency List) : 리스트로 그래프 연결 관계 표현
graph = [[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(연결된 노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)

#DFS 메서드 정의 
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)