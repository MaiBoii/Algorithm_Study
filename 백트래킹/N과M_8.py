from itertools import combinations_with_replacement

n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in combinations_with_replacement(arr, m):
    for j in i:
        print(j, end=' ')
    print()