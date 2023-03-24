import heapq
import sys
input = sys.stdin.readline

max_heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(max_heap):
            print(heapq.heappop(max_heap) * -1)
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -x)
