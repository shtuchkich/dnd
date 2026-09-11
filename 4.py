a = input()
a = list(map(int, a.split(' ')))
for i in range (0, len(a) - 1, 2):
    print(a[i + 1], a[i], end = ' ')
print(a[-1])
