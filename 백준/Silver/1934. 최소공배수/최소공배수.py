def gcd(x, y):
    if y > x:
        x, y = y, x

    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print((a * b) // gcd(a, b))


if __name__ == '__main__':
    main()