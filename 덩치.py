import sys
input=sys.stdin.readline

arr=[]
n=int(input())
for i in range(n):
    dungchi=list(map(int, input().split()))
    arr.append(dungchi)
    
answer=[1]*n
for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1]<arr[j][1]:
            answer[i]+=1

for i in answer:
    print(i,end=" ")