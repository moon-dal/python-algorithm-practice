N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]

dot.sort()

for i in range(N):
    print(dot[i][0], dot[i][1])
