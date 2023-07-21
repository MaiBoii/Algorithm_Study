import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    keylog=list(input().rstrip())
    left = []
    right = []
    for key in keylog:
        if key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append(right.pop())
        elif key == '-':
            if left:
                left.pop()
        else:
            left.append(key)
    left.extend(reversed(right))
    print(''.join(left))
