tall = [int(input()) for i in range(9)]

total = sum(tall)
n1, n2 = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if total-(tall[i]+tall[j]) == 100:
            n1, n2 = tall[i], tall[j]
            tall.remove(n1)
            tall.remove(n2)
            break

    if len(tall) == 7:
        break

tall.sort()
for i in range(len(tall)):
    print(tall[i])