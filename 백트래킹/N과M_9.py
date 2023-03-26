from itertools import permutations

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr = permutations(arr, m)
arr = sorted(list(set(arr)))
for i in arr:
    print(*i)