word = input()
word = word.upper()

alphabets = {}
for i in word:
    if i in alphabets.keys():
        alphabets[i] += 1
    else:
        alphabets[i] = 1

max_value = max(alphabets.values())
max_key = ''
count = 0
for key, value in alphabets.items():
    if value == max_value:
        count += 1
        max_key = key

if count > 1:
    print('?')
else:
    print(max_key)