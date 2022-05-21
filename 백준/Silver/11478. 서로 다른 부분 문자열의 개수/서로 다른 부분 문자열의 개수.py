s = input()

part = []
for i in range(len(s)):
    for j in range(1, len(s)-i+1):
        part.append(s[i:i+j])

res = len(list(set(part)))
print(res)