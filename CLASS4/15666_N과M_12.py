from itertools import combinations_with_replacement

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr = combinations_with_replacement(arr, m)
lst = []
for i in set(arr):
    if sorted(i) not in lst:
        lst.append(sorted(i))

for i in sorted(lst):
    for j in i:
        print(j,end=' ')
    print()