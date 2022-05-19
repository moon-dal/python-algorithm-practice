N = int(input())

time = list(map(int, input().split()))

time.sort()
# 해당 수까지 더한 합
temp_sum = 0
total_sum = 0
for i in range(N):
    temp_sum += time[i]
    total_sum += temp_sum

print(total_sum)