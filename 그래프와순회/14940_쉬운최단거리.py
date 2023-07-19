from collections import deque

n,m = map(int,input().split())
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_distance(x,y):
    distance = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx < n and ny>=0 and ny < m:
            if area