N = int(input())
# 학생들이 뽑은 번호
number = list(map(int, input().split()))
order = [1]

for i in range(1, N):
    order.append(i+1)
    order.insert(i-number[i], i+1)
    del order[-1]

print(*order)