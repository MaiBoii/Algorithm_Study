from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
cost_map = [list(map(int, input().split())) for _ in range(n)]

all_case = permutations(list(range(n)))
ans = 0
for i in all_case:
    cost = 0
    flag = True
    for j in range(n-1):
        tmp = cost_map[i[j]][i[j+1]]
        if tmp == 0:
            flag = False
            break
        else:
            cost += tmp
    tmp = cost_map[i[n-1]][i[0]]
    if tmp == 0:
        flag = False
    else:
        cost += tmp
    if flag:
        ans = cost

print(ans)