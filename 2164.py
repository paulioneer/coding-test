from collections import deque


n = int(input())

_list = [i+1 for i in range(n)]
q = deque(_list)

while len(q) > 0:
    if (len(q) == 1):
        break
    q.popleft()
    if (len(q) == 1):
        break
    q.append(q.popleft())

print(q[0])
