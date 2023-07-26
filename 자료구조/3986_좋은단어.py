n=int(input())
cnt=0
for _ in range(n):
    words = input()
    stack=[]
    for i in words:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        cnt+=1
    else:
        continue

print(cnt)