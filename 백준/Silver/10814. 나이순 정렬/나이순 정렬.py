N = int(input())

member = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    member.append([i, age, name])

member.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(member[i][1], member[i][2])
