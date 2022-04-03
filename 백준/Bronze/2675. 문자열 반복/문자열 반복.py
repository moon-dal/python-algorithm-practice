import sys

t = int(sys.stdin.readline())

while t != 0:
  r = sys.stdin.readline().strip()
  n = int(r[0])
  word = r[2:]

  for i in range(len(word)):
    print(n * word[i], end='')

  print()
  
  t -= 1