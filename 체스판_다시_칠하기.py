import sys
input=sys.stdin.readline

n,m=map(int, input().split())
origin=[]
count=[]

for i in range(n):
    origin.append(input())

if origin[0][0] == 'B':
    
