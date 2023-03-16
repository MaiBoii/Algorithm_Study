arr=[]
for i in range(5):
    n=int(input())
    arr.append(n)
print(int(sum(arr)/5))
arr.sort()
print(arr[2])