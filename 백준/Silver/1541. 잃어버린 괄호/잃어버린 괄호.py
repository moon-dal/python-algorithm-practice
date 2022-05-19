E = input().split('-')

res = []
for i in E:
    cal = 0
    plus = i.split('+')
    for j in plus:
        cal += int(j)
    res.append(cal)

total = res[0]
for i in range(1, len(res)):
    total -= res[i]

print(total)