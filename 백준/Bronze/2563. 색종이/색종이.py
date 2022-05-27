white = [[0] * 100 for _ in range(100)]
cnt = 0

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            white[x+i][y+j] = 1

for i in range(100):
    for j in range(100):
        if white[i][j] == 1:
            cnt += 1

print(cnt)