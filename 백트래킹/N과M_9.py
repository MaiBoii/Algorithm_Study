from itertools import permutations

n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

per = permutations(arr, m)
tmp=[]
for i in per:
    if i not in tmp:
        tmp.append(i)
    continue

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()