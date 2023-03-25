from itertools import product

n,m = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
for i in product(arr, repeat=m):
    for j in i:
        print(j, end=' ')
    print()