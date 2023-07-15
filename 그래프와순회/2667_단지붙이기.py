n = int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y >=n:
        return False
    
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny= y + dy[i]
            dfs(nx,ny)
        return True
    return False

cnt = 0
apart = []
# 모든 노드(위치)에 대해서 단지 번호 매기기
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            apart.append(cnt)
            cnt = 0
apart.sort()
print(len(apart))
for i in range(len(apart)):
    print(apart[i])
