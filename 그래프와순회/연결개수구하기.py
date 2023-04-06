#둘다 visited면 -1, 하나만 visited면 pass 
n,m = map(int, input().split())
node=list(range(1,n+1))
graph = []
result = 0
for i in range(m):
    uv = list(map(int, input().split()))
    graph.append(uv)
visited = [False] * (n+1)

def dfs(graph, v, visited):
    global result
    visited[v] = True
    for i in node:
        if not visited:
            dfs(graph,i,visited)

dfs(graph, 1, visited)
print(result)