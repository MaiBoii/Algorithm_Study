import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    A,B = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)

visited = [0]*(n+1)

def dfs(s):
    for i in tree[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(visited[i])