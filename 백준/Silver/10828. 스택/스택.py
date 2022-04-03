import sys

# 함수
def pushX(x):
  lst.append(x)

def doPop():
  if len(lst) == 0:
    print(-1)
  else:
    print(lst.pop())
    
def printSize():
  print(len(lst))

def isEmpty():
  if len(lst) == 0:
    print(1)
  else:
    print(0)

def printTop():
  if len(lst) == 0:
    print(-1)
  else:
    print(lst[-1])


n = int(sys.stdin.readline())
lst = []

# 명령 입력받고 실행
while n != 0:
  order = sys.stdin.readline().split()
  if order[0] == 'push':
    pushX(order[1])
  if order[0] == 'pop':
    doPop()
  elif order[0] == 'size':
    printSize()
  elif order[0] == 'empty':
    isEmpty()
  elif order[0] == 'top':
    printTop()
  
  n -= 1