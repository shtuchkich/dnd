a = input()
a = list(map(int, a.split(' ')))
for i in range (0, len(a) - 1, 2):
    print(a[i + 1], a[i], end = ' ')
if len(a) % 2 == 1: print(a[-1])
