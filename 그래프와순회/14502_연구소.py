n,m = map(int,input().split())
lab = []
temp = [[0]*m for _ in range(n)]
for _ in range(n):
    lab.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = 0
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                #비어있으면 바이러스 올려놓고 다시 재귀적 수행
                temp[nx][ny] = 2
                virus(nx,ny)

def get_safearea():
    area = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                area += 1
    return area

def dfs(cnt):
    global answer
    #울타리가 3개 있음
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        #바이러스 있는 곳부터 확산 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        answer = max(answer, get_safearea())
        return 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                cnt += 1
                dfs(cnt)
                lab[i][j] =0
                cnt -= 1
dfs(0)
print(answer)

