from itertools import permutations

n,m = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
for i in permutations(arr, m):
    for j in i:
        print(j, end=' ')
    print()