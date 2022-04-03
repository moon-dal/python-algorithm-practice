import sys

def isVPS(str):
  stack = []
  for i in str:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if len(stack) != 0 and '(' in stack:
        stack.pop()
      else:
        stack.append(i)

  if '(' in stack or ')' in stack:
    print('NO')
  else:
    print('YES')


t = int(sys.stdin.readline())

while t != 0:
  bracket = sys.stdin.readline().strip()
  isVPS(bracket)
  t -= 1