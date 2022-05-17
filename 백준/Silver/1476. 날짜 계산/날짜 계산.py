E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1
while True:
    if E == e and S == s and M == m:
        break
    e += 1
    s += 1
    m += 1
    year += 1
    if e >= 16:
        e -= 15
    if s >= 29:
        s -= 28
    if m >= 20:
        m -= 19

print(year)