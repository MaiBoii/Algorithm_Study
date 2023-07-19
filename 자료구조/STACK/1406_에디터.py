import sys
from collections import deque
input=sys.stdin.readline

inserted=deque(input().rstrip())
m=int(input().rstrip())
cursor=len(inserted)
for _ in range(m):
    cmd = input().rstrip()
    if cmd=='L':
        if cursor==0:
            continue
        else:
            cursor-=1
    elif cmd == 'D':
        if cursor==len(inserted):
            continue
        else:
            cursor += 1
    elif cmd == 'B':
        if cursor==0:
            continue
        else:
            inserted.remove(inserted[cursor-1])
            cursor-=1
    elif cmd[0] =='P':
        inserted.insert(cursor,cmd[2])
        cursor+=1
print(''.join(inserted))