import sys
input=sys.stdin.readline
arr=[]
arr2=[i for i in range(1,31)]
for i in range(28):
    n=int(input())
    arr.append(n)
non=sorted(list(set(arr2)-set(arr)))

for i in range(len(non)):
    print(non[i])