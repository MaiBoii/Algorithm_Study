while True:
    word=input()
    stack=[]
    if word == '.':
        break
    for i in word:
        if i== '(' or i=='[':
           stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']') 
        elif i == ')':
            if len(stack) != 0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')') 

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
