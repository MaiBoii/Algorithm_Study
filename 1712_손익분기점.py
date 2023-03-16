import sys
input=sys.stdin.readline

a,b,c=map(int, input().split())
count=0

if c<=b:
    print(-1)
else:
    print(int(a/(c-b))+1)