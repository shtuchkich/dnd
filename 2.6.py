a = input()
a = list(map(int, a.split(' ')))
for el in a:
    if a.count(el) == 1:
        print(el, end = ' ')