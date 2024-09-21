import heapq
import sys

n = int(input())
input = sys.stdin.readline
pq = []

for _ in range(n):
    item = int(input())
    if (item == 0):
        print(heapq.heappop(pq)[1] if len(pq) > 0 else 0)
    else:
        heapq.heappush(pq, (abs(item), item))
