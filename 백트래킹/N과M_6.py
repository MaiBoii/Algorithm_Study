from itertools import combinations

n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in combinations(arr, m):
    for j in i:
        print(j, end=' ')
    print()