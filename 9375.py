import sys,collections
input=sys.stdin.readline

t=int(input())
for i in range(t):
    arr=[]
    n=int(input())
    for j in range(n):
        a,b=input().split()
        arr.append(b)
    fashion=collections.Counter(arr)
    cnt=1

    for i in fashion:
        cnt *= (fashion[i]+1)
    print(cnt-1)