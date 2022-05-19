n1, n2 = map(int, input().split())
group1 = list(input())
group2 = list(input())
T = int(input())

group1.reverse()
ants = group1 + group2

for _ in range(T):
    for i in range(len(ants) - 1):
        if ants[i] in group1 and ants[i+1] in group2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            if ants[i+1] == group1[-1]:
                break
print(''.join(ants))