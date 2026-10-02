a = input()
a = list(map(int, a.split(' ')))
for i in range (len(a)):
    print(a[i - 1], end = ' ')