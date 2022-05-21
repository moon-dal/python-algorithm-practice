a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

res = (set_a - set_b) | (set_b - set_a)
print(len(res))