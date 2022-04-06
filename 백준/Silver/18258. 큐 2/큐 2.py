from collections import deque
import sys

q = deque([])

def qPushX(x):
  q.append(x)

def qPop():
  if len(q) == 0:
    print(-1)
  else:
    print(q.popleft())

def qSize():
  print(len(q))

def qEmpty():
  if len(q) == 0:
    print(1)
  else:
    print(0)

def qFront():
  if len(q) == 0:
    print(-1)
  else:
    print(q[0])

def qBack():
  if len(q) == 0:
    print(-1)
  else:
    print(q[-1])
    

n = sys.stdin.readline()
n = int(n)

while n != 0:
  order = sys.stdin.readline().split()

  if order[0] == 'push':
    qPushX(order[1])
  elif order[0] == 'pop':
    qPop()
  elif order[0] == 'size':
    qSize()
  elif order[0] == 'empty':
    qEmpty()
  elif order[0] == 'front':
    qFront()
  elif order[0] == 'back':
    qBack()
    
  n -= 1