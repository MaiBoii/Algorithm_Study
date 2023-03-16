import sys
input=sys.stdin.readline

n=int(input())
m=list(map(int,input().split()))
v=int(input())

print(m.count(v))