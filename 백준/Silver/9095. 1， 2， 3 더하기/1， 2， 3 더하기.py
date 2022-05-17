T = int(input())
for _ in range(T):
    n = int(input())
    case = [1, 1, 2]
    for i in range(n):
        case.append(sum(case[i:i+3]))

    print(case[n])
