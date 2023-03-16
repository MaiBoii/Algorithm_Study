import sys
input=sys.stdin.readline

n=int(input())
for j in range(1,n+1):
    if j+sum([int(i) for i in str(j)])==n:
        print(j)
        break
    if j==n:
        print(0)