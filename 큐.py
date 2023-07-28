from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd.split()[0] == 'push':
        queue.append(cmd.split()[1])
    elif cmd == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == 'size':
        print(len(queue))
        print(queue)
    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])