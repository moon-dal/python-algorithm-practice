c = int(input())

while c != 0:
  lst = list(map(int, input().split()))
  
  n = lst[0]
  score = lst[1:]
  
  count = 0
  avg = sum(score) / n
  
  for i in score:
    if i > avg:
      count += 1
    res = count / n * 100

  print("{:.3f}%".format(res))
  c -= 1