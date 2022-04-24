while True:
    try:
        n = int(input())
    except EOFError:
        break

    onlyOne = 1
    expo = 0
    while True:
        if onlyOne%n == 0:
            onlyOne = str(onlyOne)
            print(len(onlyOne))
            break
        else:
            expo += 1
            onlyOne += 10**expo