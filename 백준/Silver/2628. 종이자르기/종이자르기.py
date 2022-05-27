width, height = map(int, input().split())
cut = int(input())
w = [0, width]
h = [0, height]
for i in range(cut):
    x, y = map(int, input().split())
    if x == 0:
        h.append(y)
    else:
        w.append(y)

w.sort()
h.sort()
w_dif, h_dif = [], []
for i in range(len(w)-1):
    w_dif.append(abs(w[i] - w[i+1]))

for i in range(len(h)-1):
    h_dif.append(abs(h[i] - h[i + 1]))

print(max(w_dif) * max(h_dif))