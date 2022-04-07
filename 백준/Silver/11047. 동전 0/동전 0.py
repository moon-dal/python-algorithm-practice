N, K = map(int, input().split())

value = []

for _ in range(N):
  value.append(int(input()))

value.reverse()

count = 0
for i in value:
  # if i < K:
  count += K // i
  K = K % i

print(count)