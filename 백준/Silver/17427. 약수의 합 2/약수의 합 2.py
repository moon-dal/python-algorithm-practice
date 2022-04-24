def g(num):
    # num의 약수의 합 구하는 함수
    sum_ = 0
    for i in range(1, num+1):
        sum_ += (n//i) * i
    return sum_

n = int(input())

print(g(n))