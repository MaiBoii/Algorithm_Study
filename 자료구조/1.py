import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = dict()
for i in range(n):
    site, password = map(str, input().split())
    data[site] = password

for i in range(m):
    name = str(input().rstrip())
    print(data[name])