import sys
input=sys.stdin.readline

m=int(input())
s=set()
for i in range(m):
    tmp=input().strip().split()
    if len(tmp)==1:
        command=tmp[0]
    else:
        command,target=tmp[0],tmp[1]
        target=int(target)

    if command=="add":
        s.add(target)
    elif command=="remove":
        s.discard(target)
    elif command=="check":
        if target in s:
            print(1)
        else:
            print(0)
    elif command=="toggle":
        if target in s:
            s.discard(target)
        else:
            s.add(target)
    elif command=="all":
        s=set([i for i in range(1,21)])
    else:
        s=set()