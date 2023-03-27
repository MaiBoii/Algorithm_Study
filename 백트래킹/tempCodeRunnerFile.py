from itertools import combinations_with_replacement

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr = combinations_with_replacement(arr, m)
arr = sorted(list(set(arr)))
for i in arr:
    print(*i)