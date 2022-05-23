def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if map_arr[x][y] == 1:
        global cnt
        cnt += 1
        map_arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


N = int(input())
map_arr = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = []
cnt = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for i in res:
    print(i)