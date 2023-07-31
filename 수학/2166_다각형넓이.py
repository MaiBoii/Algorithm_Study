import sys
input = sys.stdin.readline

n=int(input())
arr = []
a,b = 0,0
for _ in range(n):
    x,y = map(int, input().split())
    arr.append((x,y))
arr.append(arr[0])
for i in range(n):
    a += arr[i][0]*arr[i+1][1]
for i in range(n):
    b += arr[i][1]*arr[i+1][0]

print(f'{abs((a-b)/2):.1f}')