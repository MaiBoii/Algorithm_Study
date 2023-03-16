import sys
from collections import deque
input=sys.stdin.readline

queue = deque()
n=int(input())

while 1:
    i=int(input())

    if i == -1:
        break;
    if i == 0 and len(queue) != 0:
        queue.popleft()
    elif i !=0 and len(queue) != n:
        queue.append(i)

if len(queue) == 0:
    print("empty")
else:
    for i in queue:
        print(i, end=' ')