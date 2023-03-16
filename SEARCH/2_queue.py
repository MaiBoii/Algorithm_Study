from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(11)
queue.append(13)
queue.pop()
queue.append(3)
queue.append(40)
queue.append(1)
queue.pop()

print(queue)
queue.reverse()
print(queue)
