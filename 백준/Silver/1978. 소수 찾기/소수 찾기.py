n = int(input())
list_ = list(map(int, input().split()))

res = 0
for i in list_:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        res += 1

print(res)