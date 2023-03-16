number=int(input())
result = 0
for i in range(1,number+1):
    cnt=0
    arr = list(map(int, str(i)))
    for i in arr:
        if (i == 3) or (i == 6) or (i == 9):
            cnt+=1
    result += cnt
print(result)
