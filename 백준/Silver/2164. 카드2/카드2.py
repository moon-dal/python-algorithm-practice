from collections import deque
import sys

q = deque([])

n = int(sys.stdin.readline())

for i in range(n):
  q.append(i+1)

while len(q) > 1:
  q.popleft()
  q.append(q[0])
  q.popleft()

print(q[0])