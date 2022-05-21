a, b = map(int, input().split())
no_listen, no_see = set(), set()

for _ in range(a):
    no_listen.add(input())

for _ in range(b):
    no_see.add(input())

both = no_listen & no_see
print(len(both))

both = list(both)
both.sort()
for i in both:
    print(i)