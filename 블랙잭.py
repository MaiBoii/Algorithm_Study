import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int, input().split())
arr=list(map(int, input().split()))
arr2=[]
res=list(combinations(arr,3))
for i in range(len(res)):
    if sum(res[i]) <= m:
        arr2.append(sum(res[i]))
print(max(arr2))