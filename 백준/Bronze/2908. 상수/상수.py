a, b = map(int, input().split())

def makeReverse(num):
  hun = num // 100
  ten = (num % 100) // 10
  one = (num%100)%10

  res = one*100 + ten*10 + hun
  return res

ra = makeReverse(a)
rb = makeReverse(b)

if ra > rb:
  print(ra)
else:
  print(rb)