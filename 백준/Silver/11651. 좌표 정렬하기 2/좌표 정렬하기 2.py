N = int(input())
dot = []
for i in range(N):
    x, y = map(int, input().split())
    x, y = y, x
    dot.append([x, y])

dot.sort()

for i in range(N):
    print(dot[i][1], dot[i][0])
