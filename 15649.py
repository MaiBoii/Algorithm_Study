from itertools import permutations

n,m = map(int, input().split())
arr=list(range(1,n+1))
tmp=list(permutations(arr,m))

for i in range(len(tmp)):
    for j in range(i):
        print(tmp[i][j])
