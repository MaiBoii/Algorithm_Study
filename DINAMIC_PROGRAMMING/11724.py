import sys,math
input=sys.stdin.readline

n=int(input())
res=math.factorial(n)
count=0
for i in str(res)[::-1]: #역순으로 배열
    if i != '0':
        break
    count +=1
print(count)