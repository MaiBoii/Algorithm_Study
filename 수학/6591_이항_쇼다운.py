import sys
input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    a,b = 1,1
    for i in range(n,max(n-m,m),-1):
        a *= i
    for i in range(1,min(m,n-m)+1):
        b *= i
    print(a//b)