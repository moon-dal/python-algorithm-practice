for _ in range(3):
    state = list(map(int, input().split()))
    total = sum(state)
    if total == 1:
        print('C')
    elif total == 2:
        print('B')
    elif total == 3:
        print('A')
    elif total == 4:
        print('E')
    else:
        print('D')