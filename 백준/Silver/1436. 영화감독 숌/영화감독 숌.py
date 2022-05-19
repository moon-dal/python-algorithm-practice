N = int(input())
cnt = 0 # 몇 번째 수인지

num = 1
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        break
    num += 1

print(num)