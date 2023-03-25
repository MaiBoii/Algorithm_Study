from itertools import product

n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in product(arr, repeat=m):
    for j in i:
        print(j, end=' ')
    print()