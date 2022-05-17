N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + arr[i][0] > N:
        memo[i] = memo[i+1]
    else:
        memo[i] = max(arr[i][1] + memo[i + arr[i][0]], memo[i+1])

print(memo[0])
