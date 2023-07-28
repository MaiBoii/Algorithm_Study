N=int(input())
S=[]
RS=[]
for _ in range(N):
    s=input()
    if s.split()[0] == 'push':
        S.append(s.split()[1])
    elif s == 'pop':
        if len(S) == 0:
            RS.append(-1)
        else:
            RS.append(S[-1])
            S.remove(S[-1])
    elif s == 'size':
        RS.append(len(S))
    elif s == 'empty':
        if len(S) == 0:
            RS.append(1)
        else:
            RS.append(0)
    elif s == 'top':
        if len(S) == 0:
            RS.append(-1)
        else:
            RS.append(S[-1])
for i in RS:
    print(i)