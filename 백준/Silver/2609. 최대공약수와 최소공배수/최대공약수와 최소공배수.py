def gcd(x, y):
    if y > x:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


a, b = map(int, input().split())

print(gcd(a, b))
print(int(a * b / gcd(a, b)))