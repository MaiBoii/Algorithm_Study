import sys
input = sys.stdin.readline
         
dict = {}
k,l = map(int,input().split())
for i in range(l):
    student = input().rstrip()
    dict[student] = i

arr = sorted(dict.items(), key= lambda x:x[1])
if k>len(arr):
    k=len(arr)
for i in range(k):
    print(arr[i][0])