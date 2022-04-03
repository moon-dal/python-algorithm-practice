import sys

k = int(sys.stdin.readline())

stack = []
while k != 0:
  num = int(sys.stdin.readline())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

  k -= 1

print(sum(stack))