N, M = map(int, input().split())

s = {}
for _ in range(N):
    k = input()
    s[k] = True

cnt = 0
for _ in range(M):
    tmp = input()
    if tmp in s:
        cnt += 1

print(cnt)